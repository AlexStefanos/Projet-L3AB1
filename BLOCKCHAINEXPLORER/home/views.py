from django.shortcuts import render

def index(request):
    #request = requete qui contient des informations
    return render(request, 'home/index.html')
