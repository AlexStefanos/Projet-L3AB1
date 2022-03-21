from django.shortcuts import render

# Create your views here.
def index_documentation(request):
    return render(request, 'documentation/index_documentation.html')