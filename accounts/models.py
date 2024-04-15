from django.db import models

class GelenArama(models.Model):
    ad = models.CharField(max_length=50)
    soyad = models.CharField(max_length=50)
    telefon = models.CharField(max_length=11)
    arama_nedeni = models.TextField()
    aciklama = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.ad}{self.soyad}"
    
class KisiRehberi(models.Model):
    ad = models.CharField(max_length=50)
    soyad = models.CharField(max_length=50)
    telefon = models.CharField(max_length=11)
    email = models.EmailField()
    sirket = models.ForeignKey('Sirket', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ad}{self.soyad}"
    
class Sirket(models.Model):
    isim = models.CharField(max_length=100)
    adres = models.CharField(max_length=200)
    email = models.EmailField()
    web = models.URLField()

    def __str__(self):
        return self.isim
