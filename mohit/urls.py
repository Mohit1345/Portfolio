from django.contrib import admin
from django.urls import path
from mohit import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home,name = "home"),
    path('research',views.research,name="research"),
    path('contact',views.contact,name="contact"),

    path('api/projects/', views.projects_api_view, name='projects_api'),
    path('api/featured-projects/', views.featured_projects_api, name='featured_projects_api'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)