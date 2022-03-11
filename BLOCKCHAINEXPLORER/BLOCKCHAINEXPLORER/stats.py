import urllib.parse
import requests
from requests.structures import CaseInsensitiveDict

url = "https://mainnet.infura.io/v3/6e5e803cf1f84b4b85e6533c11f68639"
headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

def getBlockNumber() :



    data = '{"jsonrpc":"2.0","method":"eth_blockNumber","params": [],"id":1}'


    resp = requests.post(url, headers=headers, data=data)
    json = resp.json()
    result = int(json['result'],16)
    return (result)

print(getBlockNumber())