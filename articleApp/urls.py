from django.urls import path

from articleApp import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('create/', views.create_article, name='create_article'),
    path('<int:id>/', views.article_detail, name='article_detail')
]