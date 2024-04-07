import pymongo
from random import sample

# Conneect to database
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["cityinspections"]
collection = db["names"]

zip_code = input("Enter a zip code: ")

# Find buisnees in zipcode and count them
businesses_in_zip = collection.find({"address.zip": int(zip_code)})
total_businesses = collection.count_documents({"address.zip": int(zip_code)})

if total_businesses > 0:
    print(f"Total number of businesses in zip code {zip_code}: {total_businesses}")
    
    # Select 5 random businesses and print them
    selected_businesses = sample(list(businesses_in_zip), min(5, total_businesses))   
    print(f"Randomly selected businesses in zip code {zip_code}:")
    for business in selected_businesses:
        print(business['business_name'])
        
else:
    print("Zip code not found.")
    

client.close()
