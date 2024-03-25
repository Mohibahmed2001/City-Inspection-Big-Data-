import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["city_inspections_db"] 
collection = db["inspections"]  

violation_criteria = "Violation Issued"

cities = ["BROOKLYN", "Bronx"]

violations_count = collection.count_documents({
    "address.city": {"$in": cities},
    "result": violation_criteria
})

print(f"Total business violations in Brooklyn and Bronx: {violations_count}")
