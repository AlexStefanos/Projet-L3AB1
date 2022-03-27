from rest_framework.decorators import api_view
import pymongo

@api_view(['GET'])
def getExemple(request):
    client = pymongo.MongoClient("mongodb+srv://AlexStefanos01:WGKzmuXPwn8F1O7XLI1I@blockchainexplorerclust.rjtif.mongodb.net/lastblockcollection?retryWrites=true&w=majority")

    # Database Name
    db = client["BlockchainExplorer"]

    # Collection Name
    col = db["LastBlockCollection"]

    x = col.find()

    for data in x:
        dict = data.copy()
    del dict['_id']
    return Response(dict)