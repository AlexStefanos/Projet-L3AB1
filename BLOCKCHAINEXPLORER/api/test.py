from turtle import update
from numpy import matrix
import pymongo
import json
from io import StringIO
import sys

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["BlockchainExplorer"]
collection = database["LastBlockCollection"]
collectionComplete = collection.find()
with (open('LastBlockCollection.json')) as file:
    file_data = json.load(file)
x = collection.find()
for data in x:
    dict = data.copy()
del dict['_id']
print(dict)
data = dict.get("NumberLastBlock")
print(data)