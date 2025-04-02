curl -X GET https://dynamite.paas.xero-support.com/api/clusters | grep "xerodb"

################# Get XERODB DNS and IP #################

import request_data as rq
import json
import re

file=rq.get("https://dynamite.paas.xero-support.com/api/clusters")
m=file.json()

xlist = {}

for q in range(0,len(m)):
    #print('Q'+str(q))
    for w in range(0,len(m[q]['Nodes'])):
        #print('W'+str(w))
        for e in range(0,len(m[q]['Nodes'][w]['Databases'])):
            #print('E'+str(e))
            for r in range(0,len(m[q]['Nodes'][w]['Databases'][e]['DnsEntries'])):
                #print('R'+str(r))
                if "xerodb" in m[q]['Nodes'][w]['Databases'][e]['DnsEntries'][r]:
                    #print(m[q]['Nodes'][w]['Databases'][e]['DnsEntries'][r] + ',' + m[q]['Nodes'][w]['PrivateIpAddress'])
                    shard=m[q]['Nodes'][w]['Databases'][e]['DnsEntries'][r].split('.')[0]
                    host_ag=m[q]['Nodes'][w]['Databases'][e]['DnsEntries'][r][:-1]
                    host=m[q]['Nodes'][w]['PrivateIpAddress']
                    db=m[q]['Nodes'][w]['Databases'][e]['Name']
                    cell=m[q]['Nodes'][w]['Cell']
                    xlist[shard] = {}
                    xlist[shard]["hostname_ag"] = host_ag
                    xlist[shard]["hostname"] = host
                    xlist[shard]["database"] = db
                    xlist[shard]["cell"] = cell
                else:
                    continue
with open('xerodb_hostnames.json', 'w', encoding='utf-8') as f:
    json.dump(xlist, f, ensure_ascii=False, indent=4)


################# Get XERODB DNS and IP #################



# consider updated version #

for cluster in range(0,len(result)):
    for node in range(0,len(result[cluster]['Nodes'])):
        for dbase in range(0,len(result[cluster]['Nodes'][node]['Databases'])):
            for dns in range(0,len(result[cluster]['Nodes'][node]['Databases'][dbase]['DnsEntries'])):
            	
                if re.search(r'^xerodb_\d+.db.xero.com', result[cluster]['Nodes'][node]['Databases'][dbase]['DnsEntries'][dns]):
                    
                    
                    shard=result[cluster]['Nodes'][node]['Databases'][dbase]['DnsEntries'][dns].split('.')[0]
                    host_ag=result[cluster]['Nodes'][node]['Databases'][dbase]['DnsEntries'][dns][:-1]
                    host=result[cluster]['Nodes'][node]['PrivateIpAddress']
                    db=result[cluster]['Nodes'][node]['Databases'][dbase]['Name']
                    cell=result[cluster]['Nodes'][node]['Cell']
                    xlist[shard] = {}
                    xlist[shard]["hostname_ag"] = host_ag
                    xlist[shard]["hostname"] = host
                    xlist[shard]["database"] = db
                    xlist[shard]["cell"] = cell
                else:
                    continue







---- before ----

for q in range(0,len(m)):
    #print('Q'+str(q))
    for w in range(0,len(m[q]['Nodes'])):
        #print('W'+str(w))
        for e in range(0,len(m[q]['Nodes'][w]['Databases'])):
            #print('E'+str(e))
            for r in range(0,len(m[q]['Nodes'][w]['Databases'][e]['DnsEntries'])):
                #print('R'+str(r))
                if "xerodb" in m[q]['Nodes'][w]['Databases'][e]['DnsEntries'][r]:
                    print(m[q]['Nodes'][w]['Databases'][e]['DnsEntries'][r] + ',' + m[q]['Nodes'][w]['PrivateIpAddress'])
                else:
                    print('skip')
                    
                    
