from django.test import TestCase

import requests
import plotly.express as px


apiKeyEthScan = "BC9GC2BCWXHFF4BPZYGY6RV5JED5HGB72A"
address = "0xBaD6377Dfab84aFE786833AA8BE2721997f625B6"

url = "https://api.etherscan.io/api?module=account&action=txlist&address=" + address + "&startblock=0&endblock=99999999&page=1&offset=15&sort=desc&apikey=" + apiKeyEthScan

response = requests.request("GET", url)
json = response.json()
tab = []
for i in range (15) :
    tab.append(json["result"][i]["hash"])
print(tab)




