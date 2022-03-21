from django.shortcuts import render
# Create your views here.

def stats_index(request):
    return render(request, 'stats/stats_index.html')



