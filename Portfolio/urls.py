from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("mohit.urls")),
    path('blog_effect/',include('blog_effect.urls')),
]
