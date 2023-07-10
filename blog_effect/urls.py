from django.contrib import admin
from django.urls import path
from blog_effect import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.blog_index,name = "blog_index"),
    path('<str:title>', views.blog_description, name='blog_description'),
    path('<int:blog_id>/like_post/', views.like_post, name='like_post'),
    path('<int:blog_id>/share_post/', views.share_post, name='share_post'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
