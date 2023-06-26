from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
# def blog_index(request):
#     all_blogs = Blog.objects.all()
#     all_categories = Category.objects.all()
#     context = {
#         'all_categories':all_categories,
#         'all_blogs':all_blogs,
#     }
#     return render(request,"Blogs\\blog_index.html",context)

from django.shortcuts import render
from .models import Blog, Category

def blog_index(request):
    all_blogs = Blog.objects.all()
    all_categories = Category.objects.all()
    selected_category = request.GET.get('category', 'all')  # Get the selected category from the query parameters

    if selected_category != 'all':
        all_blogs = all_blogs.filter(category__category_name=selected_category)

    context = {
        'all_blogs': all_blogs,
        'all_categories': all_categories,
        'selected_category': selected_category,
    }

    return render(request, 'Blogs\\blog_index.html', context)



def blog_description(request, title):
    blog = get_object_or_404(Blog, id=title)
    context = {
        'blog_detail':blog,
    }
    return render(request, 'Blogs\\blog_description.html', context)