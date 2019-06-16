from django.db import models
from django.urls import path
# Create your models here.

from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('regulamin/', views.regulamin, name='regulamin'),
    path('kontakt/', views.kontakt, name='kontakt'),
    path('kategorie/', views.kategorie, name='kategorie'),
    path('sportowe/', views.sportowe, name='sportowe'),
    path('historyczne/', views.historyczne, name='historyczne'),
    path('przygodowe/', views.przygodowe, name='przygodowe'),
    path('naukowe/', views.naukowe, name='naukowe'),
    path('fantasty/', views.fantasty, name='fantasty'),
    path('inne/', views.inne, name='inne'),
 
]