# import json
# from urllib import request
# import requests

# url = 'http://127.0.0.1:8000/api/get/'

# json_data = requests.get(url).json()

# print(json_data)

import pymongo

client = pymongo.MongoClient("mongodb+srv://AlexStefanos01:WGKzmuXPwn8F1O7XLI1I@blockchainexplorerclust.rjtif.mongodb.net/lastblockcollection?retryWrites=true&w=majority")

# Database Name
db = client["BlockchainExplorer"]

# Collection Name
col = db["LastBlockCollection"]

x = col.find()

for data in x:
    print(data)