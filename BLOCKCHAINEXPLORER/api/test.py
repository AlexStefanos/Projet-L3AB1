# import json
# from urllib import request
# import requests

# url = 'http://127.0.0.1:8000/api/get/'

# json_data = requests.get(url).json()

# print(json_data)
from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter
from plotly.graph_objs import histogram
import plotly.express as px
import pymongo
import numpy as np
import plotly.graph_objs as go
import io
import plotly.io as pio
from PIL import Image

from turtle import update
from numpy import matrix
import pymongo
import json
from io import StringIO
import sys
import requests
from matplotlib import pyplot


urlSentValue = "http://www.tokenview.com:8088/chart/eth/daily_sent_value_usd"
apiKey = "11d0e28c6c04190b58fd6abf1f1ad55792e34e93e61c784e5b33c836efb17f1a"
urlPrix = "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD&apikey=" + apiKey
urlNewAddress = "http://www.tokenview.com:8088/chart/eth/daily_active_address"


def getPriceEth() :
    responsePrix = requests.post(urlPrix).json()
    return responsePrix


priceEth = getPriceEth()


response = requests.request("GET", urlSentValue)
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

fig = px.line(x=x,y=y)
plot(fig)



response = requests.request("GET", urlNewAddress)
responseJson = response.json()
data = responseJson["data"]
tabTransactions = []
for i in range(len(data)-15,len(data)-1):
    for cle,valeur in data[i].items() :
        tabTransactions.append((cle,valeur))
x = []
y = []
print(tabTransactions[0][1])
for i in range (14) :
    x.append(tabTransactions[i][0])
    y.append(tabTransactions[i][1])

fig = px.line(x=x,y=y)
plot(fig)
