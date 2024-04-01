import pymongo
import random

client = pymongo.MongoClient("mongodb://localhost:27017/")  
db = client["city_inspections_db"] 
collection = db["inspections"]  

json_file_path = "/Users/jannatunnazifa/Downloads/city_inspections.json"

address_value = "FLUSHING"

business_count = collection.count_documents({
    "address.city": address_value
})

print(f"Total number of businesses in Flushing: {business_count}")

businesses_in_flushing = collection.find({"address.city": address_value})

selected_businesses = random.sample(list(businesses_in_flushing), min(5, business_count))
print("Five businesses located in flushing:")
for business in selected_businesses:
    print(business["business_name"])
    
    
violation_count = collection.count_documents({
    "address.city": address_value,
    "result": "Violation Issued"
})
        
print(f"Total number of businesses in Flushing with violations: {violation_count}")    