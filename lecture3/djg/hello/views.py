from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")

def andvsilva(request):
    return HttpResponse("Hello, @andvsilva!")

def greet(request, name):
    return HttpResponse(f"Hello, @{name.capitalize()}!")