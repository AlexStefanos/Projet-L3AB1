import collections
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
from datetime import datetime 

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

def getBlockBis(BlockNumber) : 
    json_data = {"jsonrpc":"2.0","method":"eth_getBlockByNumber","params": [BlockNumber,False],"id":1} 
    resp = session.post(url, headers=headers, json = json_data) 
    json = resp.json() 
    epoch_time =  (int(json['result']['timestamp'],16)) 
    result = { "hash": json['result']['hash'], "difficulty" : int(json['result']['difficulty'],16), "total difficulty" : int(json['result']['totalDifficulty'],16) ,"miner" : json['result']['miner'], "timestamp" : datetime.utcfromtimestamp(epoch_time).strftime('%Y-%m-%d %H:%M:%S'), "size" : int(json['result']['size'],16)} 
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
    print(json)
    FromTo = {"from" : json['result']['from'], "to" : json['result']['to'], "gasPrice" : int(json['result']['gasPrice'],16)*10**(-9), "blockNumber":int(json['result']['blockNumber'],16), "value":int(json['result']['value'],16)*10**(-18)}
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
    data = {'code': 1, 'msg': '成功', 'data': [{'addr': '0x00000000219ab540356cbb839cbe05303d7705fa', 'balance': 11352626.000069, 'txCnt': 34838}, {'addr': '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2', 'balance': 6340481.331016232, 'txCnt': 3973918}, {'addr': '0xda9dfa130df4de4673b89022ee50ff26f6ea73cf', 'balance': 2113030.0012, 'txCnt': 64}, {'addr': '0xbe0eb53f46cd790cd13851d5eff43d12404d33e8', 'balance': 1996008.2837798258, 'txCnt': 1088}, {'addr': '0x73bceb1cd57c711feac4224d062b0f6ff338501e', 'balance': 1923504.538509494, 'txCnt': 480}, {'addr': '0x9bf4001d307dfd62b26a2f1307ee0c0307632d59', 'balance': 1490000.0180927091, 'txCnt': 103}, {'addr': '0x4ddc2d193948926d02f9b1fe9e1daa0718270ed5', 'balance': 1028541.690326043, 'txCnt': 25020}, {'addr': '0x61edcdf5bb737adffe5043706e7c5bb1f1a56eea', 'balance': 929498.95358134, 'txCnt': 336}, {'addr': '0xdc24316b9ae028f1497c275eb9192a3ea0f67022', 'balance': 784665.045977826, 'txCnt': 12732}, {'addr': '0x011b6e24ffb0b5f5fcc564cf4183c5bbbc96d515', 'balance': 593103.3479250012, 'txCnt': 50}]}
    x = []
    y = []
    for i in range(10) :
        y.append(data['data'][i]["balance"])
        x.append(data['data'][i]["addr"])
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

def companiesHoldingInBtc() :
    url = "https://api.coingecko.com/api/v3/companies/public_treasury/bitcoin"

    response = requests.request("GET", url)
    Json = response.json()
    tabValue = []
    tabNamesCompanies = []
    sum_Holding = 0
    for i in range (len((Json["companies"]))) :
        tabNamesCompanies.append(Json["companies"][i]['name'])
        tabValue.append(Json["companies"][i]['total_holdings'])
        sum_Holding += Json["companies"][i]['total_holdings']

    return[tabValue,tabNamesCompanies]




client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["BlockchainExplorer"]
col = database["DrawChartsCollection"]

if(col.count() == 0) :





    jsonString = {"x_data_EthPrice" : "T", 
            "y_data_EthPrice" : None,
            "x_data_EthTxCt" : None,
            "y_data_EthTxCt" : None,
            "x_data_TopWallet" : None,
            "y_data_TopWallet" : None,
            "x_data_PieMc" : None,
            "y_data_PieMc" : None,
            "x_data_PieCompanies" : None,
            "y_data_PieCompanies" : None}



    collection = database["DrawChartsCollection"]
    collectionComplete = collection.find()
    with(open('draw.json', 'w')) as file:
        json.dump(jsonString, file)
    with(open('draw.json', 'r')) as file:
        file_data = json.load(file)
    if(isinstance(file_data, list)):
        collection.insert_many(file_data)
    else:
        collection.insert_one(file_data)


gasPrice = getGasPrice()
x = col.find()
for data in x:
    dict = data.copy()

if (drawEthChart() != [dict['x_data_EthPrice'],dict['y_data_EthPrice']]) :

    (x_data_EthChart,y_data_EthChart) = drawEthChart()
    (x_data_EthTxCt,y_data_EthTxCt) = drawTransactionsChart()
    (x_data_TopWallet,y_data_TopWallet) = drawTopAdressChart()
    (x_data_PieMC,y_data_PieMc) = drawPieTopCrypto()
    (x_data_PieCompanies,y_data_PieCompanies) = companiesHoldingInBtc()

    jsonString = {"x_data_EthPrice" : x_data_EthChart, 
            "y_data_EthPrice" : y_data_EthChart,
            "x_data_EthTxCt" : x_data_EthTxCt,
            "y_data_EthTxCt" : y_data_EthTxCt,
            "x_data_TopWallet" : x_data_TopWallet,
            "y_data_TopWallet" : y_data_TopWallet,
            "x_data_PieMc" : x_data_PieMC,
            "y_data_PieMc" : y_data_PieMc,
            "x_data_PieCompanies" : x_data_PieCompanies,
            "y_data_PieCompanies" : y_data_PieCompanies}

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

def refresh(): 
    blockNumber = getBlockNumber() 
    blockNumberHex = hex(blockNumber) 
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
         
 
refresh()