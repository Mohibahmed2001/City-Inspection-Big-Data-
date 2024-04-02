import pymongo
import random

client = pymongo.MongoClient("mongodb://localhost:27017/")  
db = client["city_inspections_db"] 
collection = db["inspections"]  


violation_criteria = "Violation Issued"

cities = ["BROOKLYN", "BRONX"]

#counts the total number of businesses in brooklyn and bronx with a violation
violations_count = collection.count_documents({
    "address.city": {"$in": cities},
    "result": violation_criteria
})

print(f"Total business violations in Brooklyn and Bronx: {violations_count}") 
print()


#finds all the businesses in brooklyn with a violation
businesses_in_brooklyn = collection.find({"address.city": "BROOKLYN","result": violation_criteria})

#counts all the businesses in brooklyn with a violation
brooklyn_count = collection.count_documents({"address.city": "BROOKLYN","result": violation_criteria})

#finds all the businesses in bronx with a violation
businesses_in_bronx = collection.find({"address.city": "BRONX","result": violation_criteria})

#counts all the businesses in brooklyn with a violation
bronx_count = collection.count_documents({"address.city": "BRONX","result": violation_criteria})

#calculates the difference
diff= brooklyn_count - bronx_count

#print the first five businesses un brookyln with a violation
print("First five businesses located in Brooklyn:")
for business in businesses_in_brooklyn[:5]:
    print(business["business_name"])
    
print()

#print the first five businesses un bronx with a violation
print("First five businesses located in Bronx:")
for business in businesses_in_bronx[:5]:
    print(business["business_name"])
    
print()
print(f"Total number of violations in Brooklyn: {brooklyn_count}")
print(f"Total number of violations in Bronx: {bronx_count}")
print(f"Difference in count: {diff}")
    

