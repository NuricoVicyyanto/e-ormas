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
from django.contrib import admin
from django.urls import path
from eormasapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('landing/', views.landing, name='landing'),

    # desa
    path('desa/', views.desa, name='desa'),
    path('tambah_desa/', views.tambah_desa, name='tambah_desa'),
    path('desa/hapus_desa/<int:id_desa>', views.hapus_desa, name='hapus_desa'),

    # kecamatan
    path('kecamatan/', views.kecamatan, name='kecamatan'),
    path('tambah_kecamatan/', views.tambah_kecamatan, name='tambah_kecamatan'),
    path('kecamatan/hapus_kecamatan/<int:id_kecamatan>', views.hapus_kecamatan, name='hapus_kecamatan'),

    # kabupaten
    path('kabupaten/', views.kabupaten, name='kabupaten'),
    path('tambah_kabupaten/', views.tambah_kabupaten, name='tambah_kabupaten'),
    path('kabupaten/hapus_kabupaten/<int:id_kabupaten>', views.hapus_kabupaten, name='hapus_kabupaten'),

    # unsur
    path('unsur_ormas/', views.unsur, name='unsur_ormas'),
    path('tambah_unsur/', views.tambah_unsur, name='tambah_unsur'),

    # ormas
    path('data_ormas/', views.data_ormas, name='data_ormas'),
    path('tambah_ormas/', views.tambah_ormas, name='tambah_ormas'),
    
    path('jml_ormas_ds/', views.jml_ormas_ds, name='jml_ormas_ds'),
    path('jml_ormas_kec/', views.jml_ormas_kec, name='jml_ormas_kec'),
    path('jml_ormas_kab/', views.jml_ormas_kab, name='jml_ormas_kab'),
]
