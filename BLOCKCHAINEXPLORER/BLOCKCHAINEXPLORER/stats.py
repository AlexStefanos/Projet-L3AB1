import urllib.parse

import requests
import json
import threading
import time
from requests.structures import CaseInsensitiveDict



url = "https://api.zmok.io/mainnet/lcf0jmfdvhdi3ezt"
url2 = "https://api.zmok.io/mainnet/uoeoajazlmlsvslh"
url3 = "https://api.zmok.io/mainnet/swmxlmavvfhtdeyl"
headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
adress = "0x9c5083dd4838e120dbeac44c052179692aa5dac5"
notReadyBegin = True
notReadyEnd = True

session = requests.Session()
session.get(url)

def getGasPrice() :

    json_data ={"jsonrpc":"2.0","method":"eth_gasPrice","params": [],"id":1}
    resp = session.post(url, headers=headers, json = json_data)
    json = resp.json()
    result = int(json['result'],16)*10**(-9)
    return (result)
    
def getBlockNumber() :

    json_data = {"jsonrpc":"2.0","method":"eth_blockNumber","params": [],"id":1}
    resp = session.post(url, headers=headers, json = json_data)
    json = resp.json()
    result = int(json['result'],16)
    return (result)

def getBalanceEth(Walletadress) :

    json_data ={"jsonrpc" : "2.0", "method" : "eth_getBalance", "params" : [ Walletadress , "latest"],"id" : 1}
    resp = session.post(url, headers=headers, json = json_data)
    json = resp.json()
    result = int(json['result'],16)*10**(-18)
    return (result)

def getBlock(BlockNumber) :
    json_data = {"jsonrpc":"2.0","method":"eth_getBlockByNumber","params": [BlockNumber,False],"id":1}
    resp = session.post(url, headers=headers, json = json_data)
    json = resp.json()
    result = json['result']['transactions']
    return (result)

def getTransactionCount(blockNumber) :
    json_data = {"jsonrpc":"2.0","method":"eth_getBlockTransactionCountByNumber","params": [blockNumber],"id":1}
    resp = session.post(url, headers=headers, json = json_data)
    json = resp.json()
    result = int(json['result'],16)
    return (result)

def getTransactionInfo(TransactionHash,Url) :
    json_data = {"jsonrpc":"2.0","method":"eth_getTransactionByHash","params": [TransactionHash],"id":1}
    resp = session.post(Url, headers=headers, json = json_data)
    json = resp.json()
    valueInEth = int(json['result']['value'],16)*10**(-18)
    return valueInEth

blockNumber = getBlockNumber()
blockNumberHex = hex(blockNumber)
numberOfTransactions = getTransactionCount(blockNumberHex)
InfoBlock = getBlock(blockNumberHex)

print("The number of the last block is : " + str(blockNumber))
print("The actual gas price is : " + str(getGasPrice()) + " Gwei") 
print("The ETH balance of the adress " + adress + " is : " + str(getBalanceEth(adress)))
print("The number of transactions in the block number " + str(blockNumber) + " is : " + str(numberOfTransactions))

tabJsonBeginningValue = []
tabJsonMiddleValue = []
tabJsonEndValue = []
tabJsonBeginningHash = []
tabJsonMiddleHash = []
tabJsonEndHash = []

def f1():
    for i in range(0,int(numberOfTransactions/3)) :
        #tabJsonBeginningValue.append(getTransactionInfo(InfoBlock[i],url))
        tabJsonBeginningHash.append(InfoBlock[i])
        
 
def f2():
    for i in range(int(numberOfTransactions/3),int(2*numberOfTransactions/3)) :
        #tabJsonMiddleValue.append(getTransactionInfo(InfoBlock[i],url2))
        tabJsonMiddleHash.append(InfoBlock[i])


def f3():
    for i in range(int(2*numberOfTransactions/3),numberOfTransactions) :
        #tabJsonEndValue.append(getTransactionInfo(InfoBlock[i],url3))
        tabJsonEndHash.append(InfoBlock[i])
 

t1 = threading.Thread(None,target=f1)
t2 = threading.Thread(None,target=f2)
t3 = threading.Thread(None,target = f3)

t1.start()
t2.start()
t3.start()

debut = time.time()

while (t1.is_alive() or t2.is_alive() or t3.is_alive()) :
    time.sleep(0.5)
fin = time.time()

print(fin-debut)

#tabJsonBeginningValue.extend(tabJsonMiddleValue)
#tabJsonBeginningValue.extend(tabJsonEndValue)

tabJsonBeginningHash.extend(tabJsonMiddleHash)
tabJsonBeginningHash.extend(tabJsonEndHash)

jsonString = {"NumberLastBlock" : str(blockNumber), 
            "GasPrice(Gwei)" : str(getGasPrice()), 
            "NbTransactions" : str(numberOfTransactions)}
# Json = json.dumps(jsonString)
# print(Json)

jsonStringHash = {"NumberBlock" : str(blockNumber), 
                "AllTransactionsHash" : str(tabJsonBeginningHash)}


import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["BlockchainExplorer"]
collection = database["LastBlockCollection"]
collectionComplete = collection.find()
with(open('data.json', 'w')) as file:
    json.dump(jsonString, file)
with(open('data.json', 'r')) as file:
    file_data = json.load(file)
if(isinstance(file_data, list)):
    collection.insert_many(file_data)
else:
    collection.insert_one(file_data)

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["BlockchainExplorer"]
collection = database["InfoHashBlock"]
collectionComplete = collection.find()
with(open('data.json', 'w')) as file:
    json.dump(jsonStringHash, file)
with(open('data.json', 'r')) as file:
    file_data = json.load(file)
if(isinstance(file_data, list)):
    collection.insert_many(file_data)
else:
    collection.insert_one(file_data)
