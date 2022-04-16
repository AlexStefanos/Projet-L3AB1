from django.test import SimpleTestCase
from api import stats
import requests

def getStatusCodeApiLlamaCharts() :
    urlTvlHistoryEth = "https://api.llama.fi/charts/Ethereum"
    response = requests.request("GET", urlTvlHistoryEth)
    return(response.status_code)

def getStatusCodeApiLlamaPie() :
    url = "https://api.llama.fi/protocols"
    response = requests.request("GET", url)
    return(response.status_code)

def getStatusCodeApiCompanies() :
    url = "https://api.coingecko.com/api/v3/companies/public_treasury/ethereum"
    response = requests.request("GET", url)
    return(response.status_code)

def getStatusCodePieGecko() :
    url = "https://api.coingecko.com/api/v3/global"
    response = requests.request("GET", url)
    return(response.status_code)

def getStatusEthPriceHistory() :
    apiKey = "11d0e28c6c04190b58fd6abf1f1ad55792e34e93e61c784e5b33c836efb17f1a"
    url = "https://min-api.cryptocompare.com/data/v2/histoday?fsym=ETH&tsym=USD&limit=365&apikey=" + apiKey
    response = requests.request("GET",url)
    return(response.status_code)

def getStatusZmok() :
    url = "https://api.zmok.io/mainnet/lcf0jmfdvhdi3ezt"
    json_data ={"jsonrpc":"2.0","method":"eth_gasPrice","params": [],"id":1}
    response = requests.post(url,json = json_data)
    return(response.status_code)



class Test(SimpleTestCase) :

    def testInfura(self) :
        self.assertEqual(stats.apiKey,"11d0e28c6c04190b58fd6abf1f1ad55792e34e93e61c784e5b33c836efb17f1a")
        self.assertEqual(stats.getBlock(hex(1000000)),['0xea1093d492a1dcb1bef708f771a99a96ff05dcab81ca76c31940300177fcf49f', '0xe9e91f1ee4b56c0df2e9f06c2b8c27c6076195a88a7b8537ba8313d80e6f124e'])
        self.assertEqual(stats.getTransactionInfo("0xa211ef5e69b6ea08ed522b3cf17b45e0a9ca5affb3de53e0fd5ac58388d12421"),1.248316865061291)
        self.assertEqual(stats.getTransactionFromTo("0xd1e899e9800022cae4daec00703c6584f143df8c26c9be7c05b29da188da8c15"), {'from': '0xf1c4d6038adf70e6d5d4272707df85e3880c6487', 'to': '0x4b4bd0af78ae288a97026bdb3907861cd42f7c17', 'gasPrice': 30.000000000000004, 'blockNumber': 14596794, 'value': 0.00264})
        self.assertEqual(stats.getTransactionCount(hex(1000000)), 2)




    def testAPIEndpoints(self) :
        self.assertEqual(200,getStatusCodeApiLlamaCharts())
        self.assertEqual(200,getStatusCodeApiLlamaPie())
        self.assertEqual(200,getStatusCodePieGecko())
        self.assertEqual(200,getStatusCodeApiCompanies())
        self.assertEqual(200,getStatusEthPriceHistory())
        self.assertEqual(200,getStatusZmok())


    