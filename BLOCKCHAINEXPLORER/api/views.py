from rest_framework.decorators import api_view
from rest_framework.response import Response
import pymongo
from . import stats
# Dans ce fichier nous avons les differents endpoints de l API

# Permet d obtenir le dernier block
@api_view(['GET'])
def getLastBlock(request):
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Database Name
    db = client["BlockchainExplorer"]

    # Collection Name
    col = db["LastBlockCollection"]
    
    x = col.find().sort("NumberLastBlock") 
    list = []
    for data in x:
        dict = data.copy()
    del dict['_id']
    return Response(dict)

# Permet d obtenir des informations sur un block passe en parametre
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

# Permet d obetenir les transaction contenu dans un block donne
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

# Permet de savoir de la source, le destinataire, le prix du gaz et la valeur d'une transaction
@api_view(['GET'])
def getFromTo(request,pk=None):
    transaction = pk
    if transaction is not None:
        dict = stats.getTransactionFromTo(transaction)
        return Response(dict)

# Permet d obtenir le montant d'un portefeuille ethereum a partir d une adresse
@api_view(['GET'])
def getWallet(request,pk=None):
    adress = pk
    if adress is not None:
        dict = stats.getBalanceEth(adress)
        return Response(dict)

# Permet d obtenir le prix de l ethereum actuellement  
@api_view(['GET'])
def getEthPrice(request):
    dict = stats.getEthPrice()
    return Response(dict)

# Permet d'avoir tout les transactions qu a pu effectuer une adresse
@api_view(['GET'])
def getAllTransactionsAdress(request,pk =None):
    adress = pk
    dict = stats.getAllTransactionAdress(adress)
    return Response(dict)

# Permet d obtenir des informations supplementaires sur un block comme ca taille et sa date
@api_view(['GET'])
def getBlockBis(request,pk =None):
    block = hex(pk)
    dict = stats.getBlockBis(block)
    return Response(dict) 

# Permet d actualiser notre base de donnee
@api_view(['GET'])
def Refresh(request):
    stats.refresh()
    dict = { "Refresh" : "OK"}
    return Response(dict)

# Permet d'avoir tout les transactions d un block
@api_view(['GET'])
def getAllTransactionsBlock(request,pk =None):
    block = hex(pk)
    dict = {"allTransactions" : stats.getBlock(block)}
    return Response(dict)
