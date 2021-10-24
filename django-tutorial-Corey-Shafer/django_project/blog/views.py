from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'andvsilva',
        'title': 'Blog Post 1',
        'content': 'First post conent',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'First post conent',
        'date_posted': 'August 28, 2018'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})