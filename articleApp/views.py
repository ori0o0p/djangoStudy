from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from articleApp.models import Article


# Create your views here.
def hello_world(request):
    return HttpResponse("hello world!")

def create_article(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        article = Article(title=title, content=content)
        article.save()
        return HttpResponse("게시물 생성완료")
    return render(request, '')