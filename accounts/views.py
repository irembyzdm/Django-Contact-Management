from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import CreateUserForm, GelenAramaForm, KisiForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # veya yönlendirilmek istenen başka bir sayfa
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')


def home(request):
    kisiler = KisiRehberi.objects.all()

    total_kisiler = kisiler.count()


    context = {'kisiler':kisiler,
               'total_kisiler':total_kisiler,
               }
    
    return render(request, 'dashboard.html',context)

def kisiler(request):
    kisiler = KisiRehberi.objects.all()
    form = KisiForm()
    context = {
        'kisiler': kisiler,
        'form': form
    }
    return render(request, 'kisiler.html', context)


def kisi_detay(request, id):
    kisi = get_object_or_404(KisiRehberi, pk=id)
    return render(request, 'kisi_detay.html', {'kisi': kisi})


def kisi_ekle(request):
    sirketler = Sirket.objects.all()
    if request.method == 'POST':
        form = KisiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kisiler')
        else:
            print(form.errors) 
    else:
        form = KisiForm()
    return render(request, 'kisi_ekle.html', {'sirketler': sirketler, 'form': form})



def anasayfa(request):
    return render(request, 'anasayfa.html')

def gelen_aramalar(request):
    aramalar = GelenArama.objects.all()
    return render(request, 'gelen_aramalar.html', {'aramalar': aramalar})

def arama_kaydi(request):
    if request.method == 'POST':
        form = GelenAramaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gelen_aramalar') 
    else:
        form = GelenAramaForm()
    return render(request, 'arama_kaydi.html', {'form': form})

def arama_detay(request, arama_id):
    arama = get_object_or_404(GelenArama, pk=arama_id)
    return render(request, 'detay.html', {'arama': arama})


def sirket_detay(request, sirket_id):
    sirket = get_object_or_404(Sirket, pk=sirket_id)
    return render(request, 'sirket_detay.html', {'sirket': sirket})


# file yapısı
# accounts
# ..templates
# ....accounts
# ......dashboard.html
# ......profile.html
# ......customer.html