from django.db import models
from django.urls import path
# Create your models here.

from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('regulamin/', views.regulamin, name='regulamin'),
    path('kontakt/', views.kontakt, name='kontakt'),
    path('kategorie/', views.kategorie, name='kategorie'),
 
]