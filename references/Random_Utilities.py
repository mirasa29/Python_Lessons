########################
##  Random Utilities  ##
########################

#=============
# CSV to JSON
#=============

import csv
import json

def csv_to_json(csvFilePath, jsonFilePath):
	
	jsonArray = []
    
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf:
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)
        
        #convert each csv row into python dict
        for row in csvReader:
            #add this python dict to json array
            jsonArray.append(row)
    
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)


# Source CSV file
csvFilePath =r'/Users/arjel.miras/Downloads/orbit_shards.txt'

# Target JSON file
jsonFilePath = r'data.json'

# Run function
csv_to_json(csvFilePath, jsonFilePath)


#========================================================================


import request as rq
import pprint as pp

endpoint = "https://dynamite.paas.xero-support.com/api/nodes"

shards = []
request = rq.get(endpoint)
pload = request.json()

# print json file as readable
pp.pprint(pload)

# print to a file 1
f = open("output.json", "w")
f.write(str(pload))
f.close()

# print to a file 2
f = open("output.json", "w")
printer = pp.PrettyPrinter(indent=4, stream=f)
pp.pprint(pload)


# Parse Dynamite Node API payload to get DB name and Cell name (contains duplicates)

for q in range(0, len(pload)):
    for w in range(0, len(pload[q]['Nodes'])):
        for e in range(0, len(pload[q]['Nodes'][w]['Databases'])):
            for r in range(0, len(pload[q]['Nodes'][w]['Databases'][e]['Name'])):
                if "XeroV3" in pload[q]['Nodes'][w]['Databases'][e]['Name']:
                    print("{},{}".format(pload[q]['Nodes'][w]['Cell'],pload[q]['Nodes'][w]['Databases'][e]['Name']))
                    shards.append(pload[q]['Nodes'][w]['Cell']+':'+pload[q]['Nodes'][w]['Databases'][e]['Name'])
                else:
                    print("SKIP!")
                    
# get unique values
mylist = list(set(shard))

# dump to file
f = open("shard_cell.list", "a")
f.write(str(mylist))
f.close()

# bash post-process

cat shard_cell.list | cut -d "," -f1-`wc -l shard_cell.list` | sed "s/'//g" | sed 's/,/\n/g' | sed 's/:/,/g' > shard_cell.csv


#========================================================================

 
