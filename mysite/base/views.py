from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')
def regulamin(request):
    return render(request, 'regulamin.html')
def kontakt(request):
    return render(request, 'kontakt.html')
def kategorie(request):
    return render(request, 'kategorie.html')

def test(request):
    return HttpResponse("test")