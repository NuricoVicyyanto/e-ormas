"""eormas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from eormasapp import views
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),

    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('landing/', views.landing, name='landing'),
    path('daftar_user/', views.daftar_user, name='daftar_user'),
    path('', views.dashboard, name='dashboard'),
    path('ormas/', views.ormas, name='ormas'),
    path('ormas_uns/', views.ormas_uns, name='ormas_uns'),
    path('ormas_ds/', views.ormas_ds, name='ormas_ds'),
    path('ormas_kec/', views.ormas_kec, name='ormas_kec'),
    path('ormas_kab/', views.ormas_kab, name='ormas_kab'),
    path('grafik/', views.grafik, name='grafik'),
    path('galeri_view/', views.galeri_view, name='galeri_view'),


    # ormas
    path('data_ormas/', views.data_ormas, name='data_ormas'),
    path('tambah_ormas/', views.tambah_ormas, name='tambah_ormas'),
    path('data_ormas/edit_ormas/<int:id_ormas>', views.edit_ormas, name='edit_ormas'),
    path('data_ormas/hapus_ormas/<int:id_ormas>', views.hapus_ormas, name='hapus_ormas'),
<<<<<<< Updated upstream
    path('data_ormas/verifikasi_ormas/<int:id_ormas>', views.verifikasi_ormas, name='verifikasi_ormas'),
=======
    path('data_ormas/verifikasi_ormas/<int:id_ormas>', views.verifikasi_edit_ormas, name='verifikasi_ormas'),
>>>>>>> Stashed changes
    
    path('jml_ormas_uns/', views.jml_ormas_uns, name='jml_ormas_uns'),
    path('jml_ormas_ds/', views.jml_ormas_ds, name='jml_ormas_ds'),
    path('jml_ormas_kec/', views.jml_ormas_kec, name='jml_ormas_kec'),
    path('jml_ormas_kab/', views.jml_ormas_kab, name='jml_ormas_kab'),

    # galeri
    path('galeri/', views.galeri, name='galeri'),
    path('tambah_galeri/', views.tambah_galeri, name='tambah_galeri'),
    path('galeri/edit_galeri/<int:id_galeri>', views.edit_galeri, name='edit_galeri'),
    path('galeri/hapus_galeri/<int:id_galeri>', views.hapus_galeri, name='hapus_galeri'),

    # informasi
    path('informasi/', views.informasi, name='informasi'),
    path('tambah_informasi/', views.tambah_informasi, name='tambah_informasi'),
    path('informasi/edit_informasi/<int:id_informasi>', views.edit_informasi, name='edit_informasi'),
    path('informasi/hapus_informasi/<int:id_informasi>', views.hapus_informasi, name='hapus_informasi'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
