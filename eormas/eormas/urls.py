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
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('landing/', views.landing, name='landing'),

    # ormas
    path('data_ormas/', views.data_ormas, name='data_ormas'),
    path('tambah_ormas/', views.tambah_ormas, name='tambah_ormas'),
    path('data_ormas/edit_ormas/<int:id_ormas>', views.edit_ormas, name='edit_ormas'),
    path('data_ormas/hapus_ormas/<int:id_ormas>', views.hapus_ormas, name='hapus_ormas'),
    
    path('jml_ormas_uns/', views.jml_ormas_uns, name='jml_ormas_uns'),
    path('jml_ormas_ds/', views.jml_ormas_ds, name='jml_ormas_ds'),
    path('jml_ormas_kec/', views.jml_ormas_kec, name='jml_ormas_kec'),
    path('jml_ormas_kab/', views.jml_ormas_kab, name='jml_ormas_kab'),

    # galeri
    path('galeri/', views.galeri, name='galeri'),
    path('tambah_galeri/', views.tambah_galeri, name='tambah_galeri'),
    path('galeri/edit_galeri/<int:id_galeri>', views.edit_galeri, name='edit_galeri'),
    path('galeri/hapus_galeri/<int:id_galeri>', views.hapus_galeri, name='hapus_galeri'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
