import pymongo
from pymongo import MongoClient

def init():
  print("Hello, boss. This is your employees diary.")
  print("Type ALL if you want to see all your employees")
  print("Type ADD if you want to add a new employee")
  print("Type SRCN if you want to search employee by name")
  print("Type SRCF if you want to search employee by family name")
  print("Type POS if you want to update employees position")
  print("Type SAL if you want to update employees position")
  print("Type SORTN if you want to sort employees by name")


CONNECTION_STRING = 'mongodb+srv://steli29:1QAZ2wsx@cluster0.jeppn.mongodb.net/test?authSource=admin&replicaSet=atlas-yglwae-shard-0&readPreference=primary&ssl=true'
client = MongoClient(CONNECTION_STRING)
mydb = client['SoftwareCompany']

collection_name = mydb["Workers"]

dblist = client.list_database_names()
if "SoftwareCompany" in dblist:
  print("The database exists.")

item_1 = {
"_id" : "U1IT00001",
"name" : "Cristopher",
"family" : "Ivanov",
"age" : 26,
"salary" : 1500,
"position" : "junior developer"
}

collection_name.insert_one(item_1)
