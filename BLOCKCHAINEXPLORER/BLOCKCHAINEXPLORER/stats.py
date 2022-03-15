import urllib.parse
import requests
from requests.structures import CaseInsensitiveDict

url = "https://api.zmok.io/mainnet/lcf0jmfdvhdi3ezt"
headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
adress = "0x9c5083dd4838e120dbeac44c052179692aa5dac5"


def getGasPrice() :

    json_data ={"jsonrpc":"2.0","method":"eth_gasPrice","params": [],"id":1}
    resp = requests.post(url, headers=headers, json = json_data)
    json = resp.json()
    result = int(json['result'],16)*10**(-9)
    return (result)
    
def getBlockNumber() :

    json_data = {"jsonrpc":"2.0","method":"eth_blockNumber","params": [],"id":1}
    resp = requests.post(url, headers=headers, json = json_data)
    json = resp.json()
    result = int(json['result'],16)
    return (result)

def getBalanceEth(Walletadress) :

    json_data ={"jsonrpc" : "2.0", "method" : "eth_getBalance", "params" : [ Walletadress , "latest"],"id" : 1}
    resp = requests.post(url, headers=headers, json = json_data)
    json = resp.json()
    result = int(json['result'],16)*10**(-18)
    return (result)

def getBlock(BlockNumber) :
    json_data = {"jsonrpc":"2.0","method":"eth_getBlockByNumber","params": [BlockNumber,False],"id":1}
    resp = requests.post(url, headers=headers, json = json_data)
    json = resp.json()
    result = json['result']['transactions']
    return (result)

def getTransactionCount(blockNumber) :
    json_data = {"jsonrpc":"2.0","method":"eth_getBlockTransactionCountByNumber","params": [blockNumber],"id":1}
    resp = requests.post(url, headers=headers, json = json_data)
    json = resp.json()
    result = int(json['result'],16)
    return (result)

def getBlockInfo(BlockNumber,indexTransaction) :
    json_data = {"jsonrpc":"2.0","method":"eth_getTransactionByBlockNumberAndIndex","params": [BlockNumber,indexTransaction],"id":1}
    resp = requests.post(url, headers=headers, json = json_data)
    json = resp.json()
    valueInEth = int(json['result']['value'],16)*10**(-18)
    return valueInEth

def getTransactionInfo(TransactionHash) :
    json_data = {"jsonrpc":"2.0","method":"eth_getTransactionByHash","params": [TransactionHash],"id":1}
    resp = requests.post(url, headers=headers, json = json_data)
    json = resp.json()
    result = json['result']
    return result

blockNumber = getBlockNumber()
blockNumberHex = hex(blockNumber)
numberOfTransactions = getTransactionCount(blockNumberHex)
index = 0
InfoBlock = getBlock(blockNumberHex)


print("The number of the last block is : " + str(blockNumber))
print("The actual gas price is : " + str(getGasPrice()) + " Gwei") 
print("The ETH balance of the adress " + adress + " is : " + str(getBalanceEth(adress)))
#print("The hash of the transaction number " + str(index) + " in the block number " + str(blockNumber) + " is : " + str(InfoTransactions))
print("The number of transactions in the block number " + str(blockNumber) + " is : " + str(numberOfTransactions))
tab = []
for i in range (50) :
    valueInEth = int(getTransactionInfo(InfoBlock[i])['value'],16)*10**(-18)  
    sender =  getTransactionInfo(InfoBlock[i])['from']
    receiver = getTransactionInfo(InfoBlock[i])['to']
    print("\n The transaction number " + str(i) + " named by the hash : " + InfoBlock[i] + " of the block number " + str(blockNumber) +  " has a value of " + str(valueInEth) + " Ethereum")
    print("\n The sender adress is " + sender + " and the receiver adress is " + receiver)
    #tab.append(getTransactionInfo(InfoBlock[i]))
#print(tab)


#print("The transaction has a value of : " +  str(getTransactionInfo(blockNumberHex,"0x0")) + " Ethereum")
