from django.shortcuts import render

from assignments.models import About
from blogs.models import Blog, Category

def home(request):
    posts = Blog.objects.filter(is_featured=False, status='Published')
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('-updated_at')

    # Fetch about us
    try:
        about = About.objects.get()
    except:
        about = None
    context = {
        'posts': posts,
        'featured_posts': featured_posts,
        'about': about,
    }
    return render(request, 'home.html', context)