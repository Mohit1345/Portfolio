from django.contrib import admin
from django.urls import path
from blog_effect import views

urlpatterns = [
    path('', views.blog_index,name = "blog_index"),
    path('<str:title>/', views.blog_description, name='blog_description'),
]