from django.http import HttpResponse
from django.shortcuts import render, redirect

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