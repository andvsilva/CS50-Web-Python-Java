from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#def home(requests):
#    return HttpResponse('Olá')

def home(request):
    return (render(request, 'home.html', {'nome': 'andvsilva'}))