import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["city_inspections_db"] 
collection = db["inspections"]  

json_file_path = "C:/Users/ericm/Desktop/mongodb-json-files-master/datasets/city_inspections.json"

# count number from 0 and with each line+1
total_inspections = 0

with open(json_file_path, 'r') as file:
    for line in file:
        total_inspections += 1

print(f"Total number of inspections in file: {total_inspections}")

# count 2015

count_2015 = collection.count_documents({
    "date": {"$regex": "2015$"}
})

print(f"Inspections performed in 2015 in MongoDB: {count_2015}")

# count 2016

count_2016 = collection.count_documents({
    "date": {"$regex": "2016$"}
})

print(f"Inspections performed in 2016 in MongoDB: {count_2016}")