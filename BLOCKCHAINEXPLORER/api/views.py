from rest_framework.decorators import api_view
from rest_framework.response import Response
import pymongo
from . import stats

@api_view(['GET'])
def getLastBlock(request):
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Database Name
    db = client["BlockchainExplorer"]

    # Collection Name
    col = db["LastBlockCollection"]

    x = col.find()

    for data in x:
        dict = data.copy()
    del dict['_id']
    return Response(dict)

@api_view(['GET'])
def getBlockInfo(request,pk=None):
    NumberLastBlock = pk
    if NumberLastBlock is not None:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["BlockchainExplorer"]
        col = db["LastBlockCollection"]
    
        y = col.find({"NumberLastBlock": str(NumberLastBlock)})

        for data in y:
            dict = data.copy()
        del dict['_id']
        return Response(dict)

@api_view(['GET'])
def getInfoHashBlock(request,pk=None):
    NumberBlock = pk
    if NumberBlock is not None:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["BlockchainExplorer"]
        col = db["InfoHashBlock"]
    
        y = col.find({"NumberBlock": str(NumberBlock)})

        for data in y:
            dict = data.copy()
        del dict['_id']
        return Response(dict)

@api_view(['GET'])
def getFromTo(request,pk=None):
    transaction = pk
    if transaction is not None:
        dict = stats.getTransactionFromTo(transaction)
        return Response(dict)

@api_view(['GET'])
def getWallet(request,pk=None):
    adress = pk
    if adress is not None:
        dict = stats.getBalanceEth(adress)
        return Response(dict)

@api_view(['GET'])
def getEthPrice(request):
    dict = stats.getEthPrice()
    return Response(dict)

@api_view(['GET'])
def getAllTransactionsAdress(request,pk =None):
    adress = pk
    dict = stats.getAllTransactionAdress(adress)
    return Response(dict)

@api_view(['GET'])
def getBlockBis(request,pk =None):
    block = hex(pk)
    dict = stats.getBlockBis(block)
    return Response(dict) 
        

