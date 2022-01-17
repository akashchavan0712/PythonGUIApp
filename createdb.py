import pymongo

print("Welcome to pyMongo")
client = pymongo.MongoClient("mongodb://localhost:27017")
print(client)
db = client['laptopStore']
# collection = db['brandDetails']

# --------------------------------------Brand Operation--------------------------------------------

'''def insertBrand():
    collection = db['brandDetails']
    brand = input("Enter The Name of The Brand")
    brand_id = int(input("Enter The ID for the brand"))
    dictionary = {"brand":brand,"brandID":brand_id}
    collection.insert_one(dictionary)

insertBrand()'''

''''def searchBrandID():
    collection = db['brandDetails']
    brand = input("Enter The Name of The Brand : ")
    one = collection.find_one({"brand":brand})
    print(one)
    print("Done")

searchBrandID()'''

''''def searchBrandName():
    collection = db['brandDetails']
    brand_id = int(input("Enter The ID for the brand : "))
    one = collection.find_one({"brandID":brand_id})
    print(one)
    print("Done")
    
searchBrandName()'''''

# --------------------------------------Employee Operations--------------------------------------------

''''def searchEmployeeDob():
    collection1 = db['employeeDetails']
    dob = input("Enter The Date of Birth of Employee")
    one = collection1.find_one({"dateOfBirth": dob})
    print(one)
    print("Done")

searchEmployeeDob()'''''
