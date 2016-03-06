from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says: Hey there world!")


def about(request):
    return HttpResponse("Rango says: this is the about page")

# Create your views here.
