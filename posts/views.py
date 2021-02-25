from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Posts

# Create your views here.
def index(request):
    # return HttpResponse('Hello postts')
    posts = Posts.objects.all()[:10]

    context = {
        'posts': posts

    }
    return render(request, 'posts/posts.html', context)

def post_detail(request, post_id):
    """ A View to show a specific post details"""
    post = get_object_or_404(Posts, pk=post_id)

    context = {
        'post': post,

    }

    return render(request, 'posts/post_detail.html', context)