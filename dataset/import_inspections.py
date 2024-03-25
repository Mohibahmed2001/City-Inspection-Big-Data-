import pymongo
import json

client = pymongo.MongoClient("mongodb://localhost:27017/")  
db = client["city_inspections_db"] 
collection = db["inspections"]  

json_file_path = "C:/Users/mohibahmed/Desktop/mongodb-json-files-master/datasets/city_inspections.json"



with open(json_file_path, 'r') as file:
    for line in file:
        item = json.loads(line)
        
        # Check if '_id' field contains '$oid' and convert it properly
        if '_id' in item  and '$oid' in item ['_id']:
            item ['_id'] = item ['_id']['$oid']
        
        # Insert the document into the collection
        collection.insert_one(item )

print("Data inserted successfully.")
