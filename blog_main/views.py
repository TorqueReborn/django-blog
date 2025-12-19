from django.shortcuts import render

from blogs.models import Blog, Category

def home(request):
    posts = Blog.objects.filter(is_featured=False, status='Published')
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('-updated_at')

    context = {
        'posts': posts,
        'featured_posts': featured_posts,
    }
    return render(request, 'home.html', context)