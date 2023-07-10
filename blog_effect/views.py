from django.shortcuts import render, get_object_or_404
from .models import *

from django.shortcuts import render
from .models import Blog, Category

def blog_index(request):
    all_blogs = Blog.objects.all()
    all_categories = Category.objects.all()
    selected_category = request.GET.get('category', 'all') 

    if selected_category != 'all':
        all_blogs = all_blogs.filter(category__category_name=selected_category)

    context = {
        'all_blogs': all_blogs,
        'all_categories': all_categories,
        'selected_category': selected_category,
    }

    return render(request, 'Blogs/blog_index.html', context)



def blog_description(request, title):
    blog = get_object_or_404(Blog, id=title)
    context = {
        'blog_detail':blog,
    }
    return render(request, 'Blogs/blog_description.html', context)



# views.py

from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from .models import Blog

def like_post(request, blog_id):
    if 'liked_posts' not in request.session:
        request.session['liked_posts'] = []
    
    blog = Blog.objects.get(id=blog_id)
    
    if request.META.get('REMOTE_ADDR') not in request.session['liked_posts']:
        blog.likes += 1
        blog.save()
        request.session['liked_posts'].append(request.META.get('REMOTE_ADDR'))
    else:
        # return HttpResponseForbidden("You have already liked this post.")
        request.session['liked_posts'].append(request.META.get('REMOTE_ADDR'))
    
    return redirect(f"/blog_effect/{blog_id}", blog_id=blog_id)
    # return render(request, 'Blogs/blog_description.html')


def share_post(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.shares += 1
    blog.save()
    return redirect(f"/blog_effect/{blog_id}", blog_id=blog_id)
