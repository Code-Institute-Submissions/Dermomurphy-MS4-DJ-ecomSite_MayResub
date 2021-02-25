from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('Hello postts')

    context = {
        
    }
    return render(request, 'posts/posts.html', context)