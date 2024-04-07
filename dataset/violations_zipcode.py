import pymongo

# Connect to the MongoDB database
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["cityinspections"]
collection = db["names"]

# Ask the user for input for a zip code
zip_code = input("Enter a zip code: ").strip()

# Convert input into an interger
businesses_with_violations = collection.count_documents({
    "address.zip": int(zip_code), 
    "result": "Violation Issued"
})
#Print number of violations issued
if businesses_with_violations > 0:
    print(f"Total number of businesses with violations in zip code {zip_code}: {businesses_with_violations}")
else:
    print("No businesses with violations found in that zip code or zip code not found.")

client.close()
