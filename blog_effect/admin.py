from django.contrib import admin
from .models import *
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)