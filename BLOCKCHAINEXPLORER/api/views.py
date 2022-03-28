from rest_framework.decorators import api_view
from rest_framework.response import Response
import pymongo

@api_view(['GET'])
def getExemple(request):
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