import urllib.parse
import requests
from requests.structures import CaseInsensitiveDict


url = "https://mainnet.infura.io/v3/6e5e803cf1f84b4b85e6533c11f68639"
headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
adress = "0x9c5083dd4838e120dbeac44c052179692aa5dac5"

def getBalanceEth(Walletadress) :

    data2 ='{"jsonrpc" : "2.0", "method" : "eth_getBalance", "params" : [ Walletadress , "latest"],"id" : 1}'
    resp2 = requests.post(url, headers=headers, data=data2)
    json = resp2.json()
    result = int(json['result'],16)*10**(-18)
    return  (result)
    

print(getBalanceEth(adress))



"""data2 ='{"jsonrpc" : "2.0", "method" : "eth_getBalance", "params" : ["0x9c5083dd4838e120dbeac44c052179692aa5dac5", "latest"],"id" : 1}'
resp2 = requests.post(url, headers=headers, data=data2)
json = resp2.json()
result = int(json['result'],16)*10**(-18)
print (result)"""
