from django.db import models

# Create your models here.

class Uzytkownicy (models.Model):
    class Meta:
        verbose_name = "Użytkownik"
        verbose_name_plural = "Użytkownicy"
    iduzytkownika = models.IntegerField()
    typ = models.IntegerField()
    imie = models.CharField(max_length=250)
    nazwisko = models.CharField(max_length=250)
    miasto = models.CharField(max_length=250)
    numertelefonu = models.IntegerField()
    email = models.EmailField()
    from_date = models.DateTimeField('godzina dodania')

class Autorzy(models.Model):
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autorzy"
    idautora = models.IntegerField()
    imie = models.CharField(max_length=250)
    nazwisko = models.CharField(max_length=250)
    email = models.EmailField()
    numerkontaktowy = models.IntegerField()

class ksiazki(models.Model):
    class Meta:
        verbose_name = "Ksiazka"
        verbose_name_plural = "Ksiazki"
    idksiazki = models.IntegerField()
    nazwa = models.CharField(max_length=250)
    ilosc = models.CharField(max_length=250)
    nrkontakowy = models.IntegerField()
    wydawca = models.CharField(max_length=250)
    pub_date = models.DateTimeField('data wydania')

class Zamowienia(models.Model):
    class Meta:
        verbose_name = "Zamowienie"
        verbose_name_plural = "Zamowienia"
    idzamowienia = models.IntegerField()
    idrodzaj = models.IntegerField()
    datasprzedazy = models.CharField(max_length=250)
    status = models.CharField(max_length=250)
    datadoreczenia = models.CharField(max_length=250)
    order_date = models.DateTimeField('date zamowienia')


class Reklamacje(models.Model):
    class Meta:
        verbose_name = "Reklamacja"
        verbose_name_plural = "Reklamacje"
    idreklamacji = models.IntegerField()
    reklamacja_date = models.DateTimeField('data reklamacji')
    status_reklamacji = models.IntegerField()
    decyzja = models.IntegerField()
	
	
class Sportowe(models.Model):
    class Meta:
        verbose_name = "Sportowe"
        verbose_name_plural = "Sportowe"
    id = models.IntegerField(primary_key=True)
    nazwa = models.CharField(max_length=250)
    wydawca = models.CharField(max_length=250)
    ilosc = models.CharField(max_length=250)
    pub_date = models.DateTimeField('data wydania')


class Historyczne(models.Model):
    class Meta:
        verbose_name = "Historyczne"
        verbose_name_plural = "Historyczne"
    id = models.IntegerField(primary_key=True)
    nazwa = models.CharField(max_length=250)
    wydawca = models.CharField(max_length=250)
    ilosc = models.CharField(max_length=250)
    pub_date = models.DateTimeField('data wydania')


class Przygodowe(models.Model):
    class Meta:
        verbose_name = "Przygodowe"
        verbose_name_plural = "Przygodowe"
    id = models.IntegerField(primary_key=True)
    nazwa = models.CharField(max_length=250)
    wydawca = models.CharField(max_length=250)
    ilosc = models.CharField(max_length=250)
    pub_date = models.DateTimeField('data wydania')


class Naukowe(models.Model):
    class Meta:
        verbose_name = "Naukowe"
        verbose_name_plural = "Naukowe"
    id = models.IntegerField(primary_key=True)
    nazwa = models.CharField(max_length=250)
    wydawca = models.CharField(max_length=250)
    ilosc = models.CharField(max_length=250)
    pub_date = models.DateTimeField('data wydania')
	

class Fantasty(models.Model):
    class Meta:
        verbose_name = "Fantast"
        verbose_name_plural = "Fantasty"
    id = models.IntegerField(primary_key=True)
    nazwa = models.CharField(max_length=250)
    wydawca = models.CharField(max_length=250)
    ilosc = models.CharField(max_length=250)
    pub_date = models.DateTimeField('data wydania')