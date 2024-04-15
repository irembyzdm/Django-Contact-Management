from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import KisiRehberi, GelenArama

class KisiForm(forms.ModelForm):
    class Meta:
        model = KisiRehberi
        fields = ['ad', 'soyad', 'telefon', 'email', 'sirket']

class GelenAramaForm(forms.ModelForm):
    class Meta:
        model = GelenArama
        fields = ['ad', 'soyad', 'telefon', 'aciklama', 'arama_nedeni']
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        