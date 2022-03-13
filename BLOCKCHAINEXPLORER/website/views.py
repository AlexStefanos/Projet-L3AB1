from django.shortcuts import render
from .models import Article
# Create your views here.

def website_index(request):
    articles = Article.objects.all()
    data = {'articles': articles}
    return render(request, 'website/website_index.html', data)

def article(request, name):
    try:
        article = Article.objects.get(title=name)
        data = {'article': article}
    except:
        data = {'message': 'l\'article que vous avez demande n\'existe pas'}
    return render(request, 'website/article.html', data)

