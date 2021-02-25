from django.shortcuts import render
from .models import Posts

# Create your views here.
def index(request):
    # return HttpResponse('Hello postts')
    posts = Posts.objects.all()[:10]

    context = {
        'posts': posts

    }
    return render(request, 'posts/posts.html', context)