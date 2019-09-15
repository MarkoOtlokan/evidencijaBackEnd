from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


USLUGA_STATUS_PLACENO = 1
USLUGA_STATUS_NEPLACENO = 2
USLUGA_STATUS_VRACENO = 3
USLUGA_STATUS_CHOICES = (
    (USLUGA_STATUS_PLACENO, 'PLACENO'),
    (USLUGA_STATUS_NEPLACENO, 'NEPLACENO'),
    (USLUGA_STATUS_VRACENO, 'VRACENO')
)

class Usluga(models.Model):
    cena = models.FloatField()
    created = models.DateTimeField(
        default=timezone.now
    )
    napomena = models.CharField(default='', max_length=500)
    radnik = models.ForeignKey('Radnik', on_delete=models.CASCADE)
    klijent = models.ForeignKey('Klijent', on_delete=models.CASCADE)
    proizvod = models.ForeignKey('Proizvod', on_delete=models.CASCADE)
    status = models.IntegerField(choices=USLUGA_STATUS_CHOICES)
    def __str__(self):
        return self.klijent + " "+ self.radnik + " " + self.proizvod;

class Proizvod(models.Model):
    cena = models.FloatField()
    naziv = models.CharField(default='', max_length=200)
    napomena = models.CharField(default='', max_length=500)
    created = models.DateTimeField(
        default=timezone.now
    )
    def __str__(self):
        return self.naziv

class Klijent(models.Model):

    ime = models.CharField(default='', max_length=30)
    prezime = models.CharField(default='', max_length=30)
    napomena = models.CharField(default='', max_length=500)
    created = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        return self.ime + " " + self.prezime

class Radnik(models.Model):

    ime = models.CharField(default='', max_length=30)
    prezime = models.CharField(default='', max_length=30)
    plata = models.FloatField()
    jmbg = models.CharField(max_length=12)
    napomena = models.CharField(default='', max_length=500)
    created = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        return self.ime + " " + self.prezime
