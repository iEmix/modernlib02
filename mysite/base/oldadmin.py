from django.contrib import admin

# Register your models here.
from .models import Uzytkownicy
from .models import Autorzy
from .models import ksiazki
from .models import Zamowienia
from .models import Reklamacje

from .models import Sportowe
from .models import Historyczne
from .models import Przygodowe
from .models import Naukowe
from .models import Fantasty

admin.site.register(Uzytkownicy)
admin.site.register(Autorzy)
admin.site.register(ksiazki)
admin.site.register(Zamowienia)
admin.site.register(Reklamacje)

admin.site.register(Sportowe)
admin.site.register(Historyczne)
admin.site.register(Przygodowe)
admin.site.register(Naukowe)
admin.site.register(Fantasty)