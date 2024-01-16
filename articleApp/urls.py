from django.urls import path

from articleApp import views

urlpatterns = [
    path('hello/', views.hello_world),
]