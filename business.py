import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["city_inspections_db"] 
collection = db["inspections"] 

json_file_path = "C:/Users/mohibahmed/mongodb-json-files-master/datasets/city_inspections.json"



#Prompt the user to input the name of a business
business_name = input("Enter the name of a business: ")

business_exists = collection.find_one({"business_name": business_name})

if business_exists:
    violation = collection.find_one({"business_name": business_name, "result": "Violation Issued"})
    if violation:
        print(f"The business '{business_name}' has a violation.")
    else:
        print(f"The business '{business_name}' does not have any violations.")
else:
    print("Business Not found.")
