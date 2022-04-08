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

# Create your views here.


"""def stats_index(request):
    return render(request, 'stats/stats_index.html')"""

def stats_index(request):
    df = px.data.tips()
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
    fig = px.line(df, x=x_data_EthPrice, y=y_data_EthPrice, title = "ETH 14D PRICE")
    plot_div = plot(fig,output_type = 'div')
    
    x_data_DailyTx = dict['x_data_EthTxCt']
    y_data_DailyTx = dict['y_data_EthTxCt']
    fig = px.line(df, x=x_data_DailyTx, y= y_data_DailyTx, title = "ETHEREUM TRANSACTION HISTORY IN 14 DAYS")
    plot_tx = plot(fig,output_type='div')
    
    x_data_TopWallet = dict['x_data_TopWallet']
    y_data_TopWallet = dict['y_data_TopWallet']
    fig = px.histogram(df, x=x_data_TopWallet,y=y_data_TopWallet,title = "TOP 10 RICHEST ADDRESS IN ETHEREUM")
    plot_TopWallet = plot(fig,output_type='div')
    
    return render(request, 'stats/stats_index.html', context={'plot_div': plot_div,'plot_tx' : plot_tx,'plot_TopWallet' : plot_TopWallet})
