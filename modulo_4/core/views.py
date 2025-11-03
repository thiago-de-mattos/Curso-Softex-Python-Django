from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("<h1>Ola, Mundo! esta é minha primeira página de Django<h1>")

def login(request):
    return HttpResponse("<h1> login <h1> " \
    "<h2>cadastrar<h2>")