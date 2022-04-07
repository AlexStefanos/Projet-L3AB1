from django.shortcuts import render

def index(request,pk):
    #request = requete qui contient des informations
    return render(request, 'block/block_index.html')
