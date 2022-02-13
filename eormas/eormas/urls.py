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
from django.urls import include, path
from eormasapp import views
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    url(r'^export/csv/$', views.file_load_view, name='export_data'),


    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),

    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('landing/', views.landing, name='landing'),

    path('daftar_user/', views.daftarUser, name='daftar_user'),
    path('data_user/hapus_user/<int:id>', views.del_user, name='hapus_user'),



    path('', views.dashboard, name='dashboard'),
    path('ormas/', views.ormas, name='ormas'),
    path('ormas_uns/', views.ormasUnsur, name='ormas_uns'),
    path('ormas_ds/', views.ormasDesa, name='ormas_ds'),
    path('ormas_kec/', views.ormasKecamatan, name='ormas_kec'),
    path('ormas_kab/', views.ormasKabupaten, name='ormas_kab'),
    path('grafik/', views.grafik, name='grafik'),
    path('galeri_view/', views.galeriView, name='galeri_view'),

    path('statistik/', views.statistik, name='statistik'),

    path('daftar/', views.daftar, name='daftar'),
    path('pendaftaran/', views.pendaftaran, name='pendaftaran'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),

    # ormas
    path('data_ormas/', views.dataOrmas, name='data_ormas'),
    path('tambah_ormas/', views.tambahOrmas,  name='tambah_ormas'),
    path('data_ormas/edit_ormas/<int:id_ormas>', views.editOrmas, name='edit_ormas'),
    path('data_ormas/hapus_ormas/<int:id_ormas>', views.hapusOrmas, name='hapus_ormas'),
    path('data_ormas/publish_ormas/<int:id_ormas>', views.publishOrmas, name='publish_ormas'),
    
    path('jml_ormas_uns/', views.jmlOrmasDesa, name='jml_ormas_uns'),
    path('jml_ormas_ds/', views.jmlOrmasDesa, name='jml_ormas_ds'),
    path('jml_ormas_kec/', views.jmlOrmasKecamatan, name='jml_ormas_kec'),
    path('jml_ormas_kab/', views.jmlOrmasKabupaten, name='jml_ormas_kab'),

    # galeri
    path('galeri/', views.galeri, name='galeri'),
    path('tambah_galeri/', views.tambahGaleri, name='tambah_galeri'),
    path('galeri/edit_galeri/<int:id_galeri>', views.editGaleri, name='edit_galeri'),
    path('galeri/hapus_galeri/<int:id_galeri>', views.hapusGaleri, name='hapus_galeri'),

    # informasi
    path('informasi/', views.informasi, name='informasi'),
    path('tambah_informasi/', views.tambahInformasi, name='tambah_informasi'),
    path('informasi/edit_informasi/<int:id_informasi>', views.editInformasi, name='edit_informasi'),
    path('informasi/hapus_informasi/<int:id_informasi>', views.hapusInformasi, name='hapus_informasi'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
