from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
def blog_index(request):
    all_blogs = Blog.objects.all()
    all_categories = Category.objects.all()
    context = {
        'all_categories':all_categories,
        'all_blogs':all_blogs,
    }
    return render(request,"Blogs\\blog_index.html",context)



def blog_description(request, title):
    blog = get_object_or_404(Blog, id=title)
    context = {
        'blog_detail':blog,
    }
    return render(request, 'Blogs\\blog_description.html', context)