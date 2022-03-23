# import json
# from urllib import request
# import requests

# url = 'http://127.0.0.1:8000/api/get/'

# json_data = requests.get(url).json()

# print(json_data)

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
for data in collectionComplete:
    print(data)
with (open('LastBlockCollection.json')) as file:
    file_data = json.load(file)
if(isinstance(file_data, list)):
    collection.insert_many(file_data)
else:
    collection.insert_one(file_data)