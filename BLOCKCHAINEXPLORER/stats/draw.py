import requests
from plotly.offline import plot
from plotly.graph_objs import Scatter
import time

apiKey = "11d0e28c6c04190b58fd6abf1f1ad55792e34e93e61c784e5b33c836efb17f1a"
urlHistoryTxCnt = "http://www.tokenview.com:8088/chart/eth/daily_tx_cnt"
urlHisto = "https://min-api.cryptocompare.com/data/v2/histoday?fsym=ETH&tsym=USD&limit=14&apikey=" + apiKey



def drawEthChart() :
    responseHisto = requests.post(urlHisto).json()
    x = []
    y = []
    for i in range (14) :
        y.append(responseHisto['Data']['Data'][i]['open'])
        epoch_time = responseHisto['Data']['Data'][i]['time']
        x.append(time.strftime('%Y-%m-%d', time.localtime(epoch_time)))
    return [x,y]

def drawtransactionsChart() : 
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