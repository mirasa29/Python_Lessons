#!/usr/bin/env python3

import os
import json
import argparse

import request_data
from request_data.auth import HTTPBasicAuth

api_action = ["resync_table", "modify_table", "modify_column"]

parser = argparse.ArgumentParser()
parser.add_argument("--group-id", required=True, help="Fivetran Group ID to discover connectors by")
parser.add_argument("--shards-file", required=True, help="Path to a shards file to perform operations on")
parser.add_argument("--action", required=True, help=f"API Action to perform.", choices=api_action)
parser.add_argument("--action-config", required=True, help="API Action extra config")
args = parser.parse_args()


class ApiRequest(object):
    """This object holds all details per api request type"""

    def __init__(self, action="", conn_id="", schema="", table="", column=""):
        self.action = action
        self.conn_id = conn_id
        self.schema = schema
        self.table = table
        self.column = column
        self.type = None
        self.required = None
        self.url = None
        self.template = None

        match action:
            case "resync_table":
                self.url = f"https://api.fivetran.com/v1/connectors/{conn_id}/schemas/tables/resync"
                self.required = ['schema', 'table']
                self.type = "post"

            case "modify_table":
                self.url = f"https://api.fivetran.com/v1/connectors/{conn_id}/schemas/{schema}/tables/{table}"
                self.required = ['schema', 'table']
                self.type = "patch"

            case "modify_column":
                self.url = f"https://api.fivetran.com/v1/connectors/{conn_id}/schemas/{schema}/tables/{table}/columns/{column}"
                self.required = ['schema', 'table', 'column']
                self.type = "patch"

            case _:
                self.exist = f"API Request {self.action} is not (yet) supported"


# Parse shards file
shards = json.load(open(args.shards_file, "rt"))

# Setup Fivetran API
if "FIVETRAN_API_KEY" not in os.environ or "FIVETRAN_API_SECRET" not in os.environ:
    parser.error("FIVETRAN_API_KEY or FIVETRAN_API_SECRET env vars missing")

api_key = os.environ["FIVETRAN_API_KEY"]
api_secret = os.environ["FIVETRAN_API_SECRET"]
auth = HTTPBasicAuth(api_key, api_secret)

headers = {
    "Authorization": f"Basic {api_key}",
    "Content-Type": "application/json",
}

# Get Connector information for the given group_id/5tran destination
group_discover_url = f"https://api.fivetran.com/v1/groups/{args.group_id}/connectors"
response = requests.get(url=group_discover_url, auth=auth)

if not response.ok:
    raise RuntimeError("Unable to query Fivetran API, are credentials correct?")

response = response.json()

connectors = []


# Only get connector ID and Name
def parse_connectors(data):
    for connector in data:
        if connector["schema"] in shards:
            yield {
                "id": connector["id"],
                "name": connector["schema"],
            }


connectors.extend(parse_connectors(response["data"]["items"]))

# loop through response page and grab the rest of the connector ID and Name
while "next_cursor" in response["data"]:
    params = {"cursor": response["data"]["next_cursor"]}

    page = requests.get(url=group_discover_url, auth=auth, params=params)

    if not page.ok:
        raise RuntimeError("Unable to query Fivetran API, are credentials correct?")

    page = page.json()

    connectors.extend(parse_connectors(page["data"]["items"]))

    response = page

print(f"INFO: Loaded {len(connectors)}/{len(shards.keys())} connectors")

# check number of connector from Fivetran and compare against shard list
if len(connectors) != len(shards.keys()):
    raise RuntimeError("We couldn't find all shards from the API")

    shards_keys = set(shards.keys())
    api_keys = set(i["name"] for i in connectors)

    print(f"INFO: Missing shards: {shards_keys.difference(api_keys)}")


def run_api(conn, config):
    """Run Fivetran API request."""

    # set vars for object from connectors list & action_config param
    required_params = config["required"]
    action = args.action
    conn_id = conn['id']
    schema = required_params.get("schema", "")
    table = required_params.get("table", "")
    column = required_params.get("column", "")

    # get api details based on action type & required params from action_config
    try:
        api_request = ApiRequest(action, conn_id, schema, table, column)
    except Exception as e:
        print("Error encountered : ", e)

    # check action_config required params against api required params
    missing = []
    for param in api_request.required:
        if param not in required_params:
            missing.append(param)

    # bail out if there's missing param
    if missing:
        raise RuntimeError(f"Missing {missing} from action config")

    api_url = api_request.url
    data = config["data"]
    request_mode = getattr(requests, api_request.type)

    try:
        response = request_mode(url=api_url, auth=auth, json=data)
    except requests.exceptions.ReadTimeout:
        return (conn["name"], response)

    if not response.ok:
        return (conn["name"], response)

    print(f"INFO: {action} api request for {conn['name']} has been queued")


action_config = json.loads(args.action_config)

failures = []

for connector in connectors:
    if failed := run_api(connector, action_config):
        failures.append(failed)

if failures:
    print("INFO: API Failures")

    for failure in failures:
        print(failure)

