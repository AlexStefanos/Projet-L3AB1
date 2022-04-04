from django.shortcuts import render

def tx_index(request, pk):
    return render(request, 'tx/tx_index.html')
