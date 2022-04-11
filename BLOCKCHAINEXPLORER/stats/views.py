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
    db = client["BlockchainExplorer"]
    col = db["DrawChartsCollection"]
    x = col.find()
    for data in x:
        dict = data.copy()
    del dict['_id']
    x_data_EthPrice = dict['x_data_EthPrice']
    y_data_EthPrice = dict['y_data_EthPrice']
    fig = px.line(df, x=x_data_EthPrice, y=y_data_EthPrice, labels = {'x' : "Day",'y' : "Price"})
    plot_div = plot(fig,output_type = 'div')
    
    x_data_DailyTx = dict['x_data_EthTxCt']
    y_data_DailyTx = dict['y_data_EthTxCt']
    fig = px.line(df, x=x_data_DailyTx, y= y_data_DailyTx, labels = {'x' : "Day",'y' : "Amount of Transactions"})
    plot_tx = plot(fig,output_type = 'div')
    
    x_data_TopWallet = dict['x_data_TopWallet']
    y_data_TopWallet = dict['y_data_TopWallet']
    fig = px.histogram(df, x=x_data_TopWallet,y=y_data_TopWallet,  labels = {'x' : "Wallet Addresses",'y' : "Amount in Eth"})
    plot_TopWallet = plot(fig,output_type = 'div')

    x_data_PieMc = dict['x_data_PieMc']
    y_data_PieMc = dict['y_data_PieMc']
    fig = px.pie(df,values=x_data_PieMc, names=y_data_PieMc)
    plot_PieMc = plot(fig,output_type = 'div')

    x_data_PieCompanies = dict['x_data_PieCompanies']
    y_data_PieCompanies = dict['y_data_PieCompanies']
    fig = px.pie(df,values=x_data_PieCompanies, names=y_data_PieCompanies)
    plot_PieCompanies = plot(fig,output_type = 'div')

    return render(request, 'stats/stats_index.html', context={'plot_div': plot_div,'plot_tx' : plot_tx,'plot_TopWallet' : plot_TopWallet,'plot_PieMc' : plot_PieMc, 'plot_PieCompanies' : plot_PieCompanies})


