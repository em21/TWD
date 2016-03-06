from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    context_dict = {'bold message': "I am bold font from the context"}
    return render(request, 'rango/index.html', context_dict)


def about(request):
    return HttpResponse("Rango says: this is the about page")

# Create your views here.
