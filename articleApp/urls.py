from django.urls import path

from articleApp import views

urlpatterns = [
    path('articles/', views.article_list, name='article_list')
    
]