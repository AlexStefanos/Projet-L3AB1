from django.shortcuts import render

def adress_index(request, pk):
    return render(request, 'adress/index_adress.html')



