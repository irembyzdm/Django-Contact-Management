from django.contrib import admin
from .models import GelenArama, KisiRehberi, Sirket

# GelenArama modelini admin paneline kaydetme
@admin.register(GelenArama)
class GelenAramaAdmin(admin.ModelAdmin):
    list_display = ['ad', 'soyad', 'telefon', 'aciklama', 'arama_nedeni']

# KisiRehberi modelini admin paneline kaydetme
@admin.register(KisiRehberi)
class KisiRehberiAdmin(admin.ModelAdmin):
    list_display = ['ad', 'soyad', 'telefon', 'email', 'sirket']

# Sirket modelini admin paneline kaydetme
@admin.register(Sirket)
class SirketAdmin(admin.ModelAdmin):
    list_display = ['isim', 'adres', 'email', 'web']
