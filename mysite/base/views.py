from django.shortcuts import render
from django.http import HttpResponse
from .models import Sportowe, Historyczne, Przygodowe, Naukowe, Fantasty, Inne
# Create your views here.

def index(request):
    return render(request, 'index.html')
def regulamin(request):
    return render(request, 'regulamin.html')
def kontakt(request):
    return render(request, 'kontakt.html')
def kategorie(request):
    return render(request, 'kategorie.html')
def komentarze(request):
    return render(request, 'komentarze.html')
def sportowe(request):
    return render(request, 'sportowe.html', {'Sportowe': Sportowe.objects.all()})
def historyczne(request):
    return render(request, 'historyczne.html', {'Historyczne': Historyczne.objects.all()})
def przygodowe(request):
    return render(request, 'przygodowe.html', {'Przygodowe': Przygodowe.objects.all()})
def naukowe(request):
    return render(request, 'naukowe.html', {'Naukowe': Naukowe.objects.all()})
def fantasty(request):
    return render(request, 'fantasty.html', {'Fantasty': Fantasty.objects.all()})
def inne(request):
    return render(request, 'inne.html', {'Inne': Inne.objects.all()})

def test(request):
    return HttpResponse("test")