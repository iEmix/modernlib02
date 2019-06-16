"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('base.urls')),
    path('index/', include('base.urls')),
    path('kontakt/', include('base.urls')),
    path('regulamin/', include('base.urls')),
    path('sportowe/', include('base.urls')),
    path('historyczne/', include('base.urls')),
    path('przygodowe/', include('base.urls')),
    path('naukowe/', include('base.urls')),
    path('fantasty/', include('base.urls')),
    path('inne/', include('base.urls')),
    path('komentarze/', include('base.urls')),
    path('admin/', admin.site.urls),
]