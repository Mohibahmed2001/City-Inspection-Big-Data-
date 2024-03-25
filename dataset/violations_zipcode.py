import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["city_inspections_db"]
collection = db["inspections"]

json_file_path = "C:/Users/mohibahmed/mongodb-json-files-master/datasets/city_inspections.json"

# Ask user for zip code
zip_code = input("Enter a zip code: ")

# List the buisnesses that have violations issued
businesses_with_violations = collection.count_documents({"address.zip": zip_code, "result": "Violation Issued"})
if businesses_with_violations > 0:
    print(f"Total number of businesses with violations in zip code {zip_code}: {businesses_with_violations}")
else:
    print("Zip code not found.")
