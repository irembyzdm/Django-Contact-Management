from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.home, name="home"),
    path('kisiler/', views.kisiler, name="kisiler"),
    path('kisi/<int:id>/', views.kisi_detay, name='kisi_detay'),
    path('kisi_ekle/', views.kisi_ekle, name='kisi_ekle'),
    path('gelen_aramalar/', views.gelen_aramalar, name="gelen_aramalar"),
    path('aramalar/<int:arama_id>/', views.arama_detay, name='arama_detay'),
    path('arama_kaydi/', views.arama_kaydi, name="arama_kaydi"),
    path('sirket/<int:sirket_id>/', views.sirket_detay, name='sirket_detay'),
]