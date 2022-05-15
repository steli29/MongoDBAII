import pymongo
from pymongo import MongoClient

def getAll():
  for worker in collection_name.find():
    print(worker)

def addWorker():
  print('Input name')
  name = input()
  print('Input family name')
  familyName = input()
  print('Input age')
  age = input()
  print('Input salary')
  salary = input()
  print('Input position')
  position = input()
  newWorker = {
    "name": name,
    "family": familyName,
    "age": age,
    "position": position,
    "salary": salary
  }
  collection_name.insert_one(newWorker)

def searchByName(name):
  query = {"name": name}
  for worker in collection_name.find(query):
    print(worker)

def searchByFamily(family):
  query = {"family": family}
  for worker in collection_name.find(query):
    print(worker)


def updateWorkerByPosition(name, family, newPosition):
  query = {
    "name": name,
    "family": family,
  }

  worker = collection_name.find_one(query)
  newValues = {"$set": {"position": newPosition}}
  collection_name.update_one(worker, newValues)

def updateWorkerBySalary(name, family, newSalary):
  query = {
    "name": name,
    "family": family,
  }

  worker = collection_name.find_one(query)
  newValues = {"$set": {"salary": newSalary}}
  collection_name.update_one(worker, newValues)

def deleteWorker(name, family):
  query = {"name": name, "family": family}
  collection_name.delete_one(query)

def sortByName():
  workers = collection_name.find().sort("name", 1)
  for worker in workers:
    print(worker)

def init():
  print("Hello, boss. This is your employees diary.")
  print("Type ALL if you want to see all your employees")
  print("Type ADD if you want to add a new employee")
  print("Type SRCN if you want to search employee by name")
  print("Type SRCF if you want to search employee by family name")
  print("Type POS if you want to update employees position")
  print("Type SAL if you want to update employees salary")
  print('Type DEL if you want to delete an employee')
  print("Type SORTN if you want to sort employees by name")
  userInput = input()
  if(userInput == 'exit'):
    print('Goodbye!')
  else:
    if(userInput == 'ALL'):
      getAll()
    elif(userInput == 'ADD'):
      addWorker()
    elif(userInput == 'SRCN'):
      print('Input name')
      name = input()
      searchByName(name)
    elif(userInput == 'SRCF'):
      print('Input family')
      family = input()
      searchByFamily(family)
    elif(userInput == 'POS'):
      print('Input name')
      name = input()
      print('Input family name')
      familyName = input()
      print('Input new position')
      position = input()
      updateWorkerByPosition(name, familyName, position)
    elif(userInput == 'SAL'):
      print('Input name')
      name = input()
      print('Input family name')
      familyName = input()
      print('Input new salary')
      salary = input()
      updateWorkerBySalary(name, familyName, salary)
    elif(userInput == 'DEL'):
       print('Input name')
       name = input()
       print('Input family name')
       familyName = input()
       deleteWorker(name, familyName)
    elif(userInput == 'SORTN'):
      sortByName()
  
  init()

CONNECTION_STRING = 'mongodb+srv://steli29:1QAZ2wsx@cluster0.jeppn.mongodb.net/test?authSource=admin&replicaSet=atlas-yglwae-shard-0&readPreference=primary&ssl=true'
client = MongoClient(CONNECTION_STRING)
mydb = client['SoftwareCompany']
collection_name = mydb["Workers"]

init()