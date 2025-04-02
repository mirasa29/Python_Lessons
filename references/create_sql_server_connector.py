import http.client
import json, csv
import sys
import argparse

from click import password_option

# create a new connector
def create_connector(
        destination_id, host_ip_address, shard_id, username, password, base64_api_key
):
    conn = http.client.HTTPSConnection("api.fivetran.com")
    payload = json.dumps(
        {
            "service": "sql_server",
            "group_id": destination_id,
            "paused": "true",
            "pause_after_trial": "false",
            "trust_fingerprints": "true",
            "trust_certificates": "true",
            "run_setup_tests": "true",
            "sync_frequency": "15",
            "config": {
                "schema_prefix": "xerodb_" + shard_id,
                "host": host_ip_address,
                "port": 1433,
                "database": "XeroV3_" + shard_id,
                "user": username,
                "password": password,
                "always_encrypted": "false",
                "tunnel_host": "prod-app1-ssh.privatelink.xero-prod.com",
                "tunnel_port": 22,
                "tunnel_user": "fivetran",
            },
        }
    )

    headers = {
        "Authorization": "Basic " + base64_api_key,
        "Content-Type": "application/json",
    }

    conn.request("POST", "/v1/connectors", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(f'response: {data.decode("utf-8")}')


# obtain the list of shard details from the csv
def get_list_of_shards(file_name):
    list_of_shards = []

    with open(file_name, encoding="utf-8", newline="") as csvf:
        csvReader = csv.DictReader(csvf)
        for row in csvReader:
            list_of_shards.append(row)

    return list_of_shards


# parse the command line arguments
def parse_args():
    parser = argparse.ArgumentParser(
        description="program used to create connectors via the fivetran api"
    )
    parser.add_argument(
        "-f", "--file", required=True, help="csv file that contains the list of shards"
    )
    parser.add_argument(
        "-d", "--destination", required=True, help="fivetran destination id"
    )
    parser.add_argument("-u", "--username", required=True, help="database username")
    parser.add_argument("-p", "--password", required=True, help="database password")
    parser.add_argument("-a", "--api_key", required=True, help="api key in base64")

    return parser.parse_args()


# main function
def main():
    list_of_shards = []
    shards_csv = None
    destination_id = None
    host_ip_address = None
    shard_id = None
    username = None
    password = None
    api_key = None
    shard_host = None

    try:
        args = parse_args()

        list_of_shards = get_list_of_shards(args.file)
        destination_id = args.destination
        username = args.username
        password = args.password
        api_key = args.api_key

        for shard in list_of_shards:
            host_ip_address = shard["ip"]
            shard_id = shard["shard_id"]

            print(
                f"fivetran_destination_id: '{destination_id}', host_ip_address: '{host_ip_address}', database_shard_id: '{shard_id}', database_username: {username}, database_password: '******'"
            )
            create_connector(
                destination_id, host_ip_address, shard_id, username, password, api_key
            )

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()