import pymongo
import random

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["city_inspections_db"]
collection = db["inspections"]

json_file_path = "C:/Users/mohibahmed/Desktop/mongodb-json-files-master/datasets/city_inspections.json"


# Ask user for zip code
zip_code = input("Enter a zip code: ")
businesses_in_zip = collection.find({"address.zip": zip_code})

# List buisnesses that are found
if businesses_in_zip.count() > 0:
    total_businesses = businesses_in_zip.count()
    print(f"Total number of businesses in zip code {zip_code}: {total_businesses}")
    selected_businesses = random.sample(list(businesses_in_zip), min(5, total_businesses))
    print("Randomly selected businesses:")
    for business in selected_businesses:
        print(business["business_name"])
else:
    print("Zip code not found.")
