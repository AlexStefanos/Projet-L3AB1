from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter
import pymongo

# Create your views here.

"""def stats_index(request):
    return render(request, 'stats/stats_index.html')"""

def stats_index(request):
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Database Name
    db = client["BlockchainExplorer"]

    # Collection Name
    col = db["DrawChartsCollection"]

    x = col.find()

    for data in x:
        dict = data.copy()
    del dict['_id']
    x_data_EthPrice = dict['x_data_EthPrice']
    y_data_EthPrice = dict['y_data_EthPrice']
    plot_div = plot([Scatter(x=x_data_EthPrice, y=y_data_EthPrice,
                        mode='lines', name='14D ETH CHART',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    x_data_DailyTx = dict['x_data_EthTxCt']
    y_data_DailyTx = dict['y_data_EthTxCt']
    plot_tx = plot([Scatter(x=x_data_DailyTx, y= y_data_DailyTx,
                        mode='lines', name='14D TX CHART',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    return render(request, 'stats/stats_index.html', context={'plot_div': plot_div,'plot_tx' : plot_tx})
