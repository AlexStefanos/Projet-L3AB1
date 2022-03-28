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

# Database Name
db = client["BlockchainExplorer"]

# Collection Name
col = db["LastBlockCollection"]

x = col.find()

for data in x:
    dict = data.copy()
del dict['_id']

print(dict)