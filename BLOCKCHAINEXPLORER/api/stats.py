import urllib.parse
import pymongo
import requests
import json
import threading
import time
from requests.structures import CaseInsensitiveDict
import requests
import time
import datetime
import matplotlib.pyplot as plt
import math
import seaborn as sns
import matplotlib.ticker

sns.set()


url = "https://api.zmok.io/mainnet/lcf0jmfdvhdi3ezt"
url2 = "https://api.zmok.io/mainnet/uoeoajazlmlsvslh"
url3 = "https://api.zmok.io/mainnet/swmxlmavvfhtdeyl"
urlHistoryTxCnt = "http://www.tokenview.com:8088/chart/eth/daily_tx_cnt"
apiKey = "11d0e28c6c04190b58fd6abf1f1ad55792e34e93e61c784e5b33c836efb17f1a"
apiKeyEthScan = "BC9GC2BCWXHFF4BPZYGY6RV5JED5HGB72A"
urlPrix = "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD&apikey=" + apiKey
urlHisto = "https://min-api.cryptocompare.com/data/v2/histoday?fsym=ETH&tsym=USD&limit=14&apikey=" + apiKey
headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
adress = "0x9c5083dd4838e120dbeac44c052179692aa5dac5"
notReadyBegin = True
notReadyEnd = True

session = requests.Session()
session.get(url)

def getEthPrice():
    apiKey = "11d0e28c6c04190b58fd6abf1f1ad55792e34e93e61c784e5b33c836efb17f1a"
    urlPrix = "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD&apikey=" + apiKey

    responsePrix = requests.post(urlPrix).json()
    return responsePrix
    

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
    json = {"EthWalletBalance" : str(result)}
    return (json)

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

def getTransactionFromTo(TransactionHash) :
    json_data = {"jsonrpc":"2.0","method":"eth_getTransactionByHash","params": [TransactionHash],"id":1}
    resp = session.post(url, headers=headers, json = json_data)
    json = resp.json()
    FromTo = {"from" : json['result']['from'], "to" : json['result']['to']}
    return (FromTo)

def getPriceEth() :
    responsePrix = requests.post(urlPrix).json()
    return responsePrix

def getAllTransactionAdress(Adress) :
    urlInfo = "https://api.etherscan.io/api?module=account&action=txlist&address=" + Adress + "&startblock=0&endblock=99999999&page=1&offset=1000&sort=asc&apikey=" + apiKeyEthScan
    responseInfo = requests.post(urlInfo).json()
    tabInfoWallet = []
    tailleTableau = len(responseInfo['result'])
    for i in range (tailleTableau) :
        tabInfoWallet.append(responseInfo['result'][i]['hash'])
    AllTransactionsWallet = {"AllTransactions" : tabInfoWallet}
    return (AllTransactionsWallet)


"""plt.plot(drawEthChart())
plt.ylabel('ETH Price')
plt.show() 
Enlever les guillemets pour tracer la courbe de l'ETH sur 14 jours"""
# print(getPriceEth()) renvoie le prix de l'ETH
# print(getAllTransactionAdress(Adress)) renvoie sous un dictionnaire l'ensemble des Hash des transactions d'une adresse 

"""blockNumber = getBlockNumber()
blockNumberHex = hex(blockNumber)
numberOfTransactions = getTransactionCount(blockNumberHex)
InfoBlock = getBlock(blockNumberHex)"""


blockNumber = getBlockNumber()
blockNumberHex = hex(blockNumber)

print("The number of the last block is : " + str(blockNumber))
"""print("The actual gas price is : " + str(getGasPrice()) + " Gwei") 
print("The ETH balance of the adress " + adress + " is : " + str(getBalanceEth(adress)))
print("The number of transactions in the block number " + str(blockNumber) + " is : " + str(numberOfTransactions))"""


"""tabJsonBeginningValue = []
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
#tabJsonBeginningValue.extend(tabJsonEndValue)"""

"""tabJsonBeginningHash.extend(tabJsonMiddleHash)
tabJsonBeginningHash.extend(tabJsonEndHash)

jsonString = {"NumberLastBlock" : str(blockNumber), 
            "GasPrice(Gwei)" : str(getGasPrice()), 
            "NbTransactions" : str(numberOfTransactions)}"""
# Json = json.dumps(jsonString)
# print(Json)

"""jsonStringHash = {"NumberBlock" : str(blockNumber), 
                "NumberTransactionsInBlock" : str(numberOfTransactions),
                "AllTransactionsHash" : str(tabJsonBeginningHash)}"""
                


def drawEthChart() :
    responseHisto = requests.post(urlHisto).json()
    x = []
    y = []
    for i in range (14) :
        y.append(responseHisto['Data']['Data'][i]['open'])
        epoch_time = responseHisto['Data']['Data'][i]['time']
        x.append(time.strftime('%Y-%m-%d', time.localtime(epoch_time)))
    return [x,y]

def drawTransactionsChart() : 
    response = requests.request("GET", urlHistoryTxCnt)
    responseJson = response.json()
    data = responseJson["data"]
    tabTransactions = []
    for i in range(len(data)-15,len(data)-1):
        for cle,valeur in data[i].items() :
            tabTransactions.append((cle,valeur))
    x = []
    y = []
    for i in range (14) :
        x.append(tabTransactions[i][0])
        y.append(tabTransactions[i][1])

    return [x,y]

def drawTopAdressChart() :
    url = "https://services.tokenview.com/vipapi/address/richrange/eth/1/10?apikey=ft7EW5mB9j7EPk3hiRUt"
    x = []
    y = []
    response = requests.request("GET", url)
    Json = response.json()
    for i in range(10) :
        y.append(Json['data'][i]["balance"])
        x.append(Json['data'][i]["addr"])
    return [x,y]
    
def drawPieTopCrypto() :
    url = "https://api.coingecko.com/api/v3/global"
    response = requests.request('GET', url)
    json = response.json()
    percentage = 0
    tabNomCrypto = []
    tabValeur = []
    for cle,valeur in json['data']["market_cap_percentage"].items() :
        percentage += valeur
        tabNomCrypto.append(cle)
        tabValeur.append(valeur)

    tabValeur.append(100-percentage)
    tabNomCrypto.append('others')
    return[tabValeur,tabNomCrypto]

def getTransactionsOfAddress(address) : 
    url = "https://api.etherscan.io/api?module=account&action=txlist&address=" + address + "&startblock=0&endblock=99999999&page=1&offset=15&sort=desc&apikey=" + apiKeyEthScan
    response = requests.request("GET", url)
    json = response.json()
    tabHash = []
    for i in range(15) :
        tabHash.append(json["result"][i]["hash"])
    AllHashTx = {"AllHashTx" : tabHash}
    return AllHashTx

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["BlockchainExplorer"]
col = database["DrawChartsCollection"]
x = col.find()
gasPrice = getGasPrice()

for data in x:
    dict = data.copy()


if (drawEthChart() != [dict['x_data_EthPrice'],dict['y_data_EthPrice']]) :

    (x_data_EthChart,y_data_EthChart) = drawEthChart()
    (x_data_EthTxCt,y_data_EthTxCt) = drawTransactionsChart()
    (x_data_TopWallet,y_data_TopWallet) = drawTopAdressChart()
    (x_data_PieMC,y_data_PieMc) = drawPieTopCrypto()


    jsonString = {"x_data_EthPrice" : x_data_EthChart, 
            "y_data_EthPrice" : y_data_EthChart,
            "x_data_EthTxCt" : x_data_EthTxCt,
            "y_data_EthTxCt" : y_data_EthTxCt,
            "x_data_TopWallet" : x_data_TopWallet,
            "y_data_TopWallet" : y_data_TopWallet,
            "x_data_PieMc" : x_data_PieMC,
            "y_data_PieMc" : y_data_PieMc}

    collection = database["DrawChartsCollection"]
    collectionComplete = collection.find()
    with(open('data.json', 'w')) as file:
        json.dump(jsonString, file)
    with(open('data.json', 'r')) as file:
        file_data = json.load(file)
    if(isinstance(file_data, list)):
        collection.insert_many(file_data)
    else:
        collection.insert_one(file_data)

for i in range(15,-1,-1) :
    txCount = getTransactionCount(hex(blockNumber-i))
    jsonString = {"NumberLastBlock" : str(blockNumber-i), 
            "GasPrice(Gwei)" : str(gasPrice), 
            "NbTransactions" : str(txCount)}
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
    
    InfoBlock = getBlock(hex(blockNumber-i))
    jsonStringHash = {"NumberBlock" : str(blockNumber-i), 
                "NumberTransactionsInBlock" : str(txCount),
                "AllTransactionsHash" : str(InfoBlock)}
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