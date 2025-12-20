from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.db.models import Q
from .models import Blog, Category

def posts_by_category(request, category_id):
    # Fetch the posts that belong to the category with
    # The id category_id
    posts = Blog.objects.filter(status='Published', category=category_id)
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')
    context = {
        'posts': posts,
        'category': category
    }
    print(context)
    return render(request, 'posts_by_categories.html', context)

def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    context = {
        'single_blog': single_blog,
    }
    print(single_blog)
    return render(request, 'blogs.html', context)

def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published')
    context = {
        'blogs': blogs,
        'keyword': keyword,
    }
    return render(request, 'search.html', context)