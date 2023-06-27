from django.contrib import admin
from django.urls import path
from blog_effect import views

urlpatterns = [
    path('blog_effect/', views.blog_index,name = "blog_index"),
    path('blog_effect/<str:title>/', views.blog_description, name='blog_description'),
]
