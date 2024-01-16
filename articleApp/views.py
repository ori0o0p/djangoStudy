import json

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from articleApp.models import Article


# Create your views here.
def hello_world(request):
    return HttpResponse("hello world!")

def create_article(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data['title']
        content = data['content']
        article = Article(title=title, content=content)
        article.save()
        return HttpResponse("생성완료")
    return render(request, '')

def article_list(request):
    articles = Article.objects.all()
    return render(request, '', {"articles": articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, '', {"article": article})
