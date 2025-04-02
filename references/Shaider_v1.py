import request_data as rq

dyna_endpoint = "https://dynamite.paas.xero-support.com/api/clusters"


def get_shards(endpoint):

    shards = []
    request = rq.get(endpoint)
    pload = request.json()

    for q in range(0, len(pload)):
        for w in range(0, len(pload[q]['Nodes'])):
            for e in range(0, len(pload[q]['Nodes'][w]['Databases'])):
                for r in range(0, len(pload[q]['Nodes'][w]['Databases'][e]['DnsEntries'])):
                    if "xerodb" in pload[q]['Nodes'][w]['Databases'][e]['DnsEntries'][r]:
                        print(pload[q]['Nodes'][w]['Databases'][e]['DnsEntries'][r])
                        shards.append(pload[q]['Nodes'][w]['Databases'][e]['DnsEntries'][r].rstrip('.'))
                    else:
                        print('skip')

    shards = list(set(shards))
    return shards


def gen_con_tf():

    dbshards = get_shards(dyna_endpoint)

    for l in dbshards:
        shard_host = l
        shard_nm = l.split(".")[0]
        s = """resource "fivetran_connector" "xerodb" {{
        group_id = "greedily_saddle"
        paused = true
        pause_after_trial = false
        run_setup_tests = true
        service = "sql_server"
        sync_frequency = 60
        trust_certificates = true
        trust_fingerprints = true
                
        destination_schema {{
        prefix = "{shard_nm}"
        }}
                
        config {{
            # schema prefix??
            host        = "{shard_host}"
            port        = 1433
            database    = "{shard_nm}"
            user        = "XADEPlatformUser"
            password    = "test_password"
            tunnel_host = "ssh-app1-uat.db.xero.com"
            tunnel_port = 22
            tunnel_user = "fivetran_user"
        }}
    }}
        """.format(shard_nm=shard_nm, shard_host=shard_host)
        f = open('./MSSQL/xerodb/'+shard_nm+'_connector.tf', "w")
        f.write(s)
        f.close()


if __name__ == '__main__':
    gen_con_tf()
