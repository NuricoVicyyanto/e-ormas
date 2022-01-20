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
    path('home/', views.home, name='home'),
    path('data_ormas/', views.data_ormas, name='data_ormas'),
    path('unsur_ormas/', views.unsur_ormas, name='unsur_ormas'),
    path('jml_ormas_ds/', views.jml_ormas_ds, name='jml_ormas_ds'),
    path('jml_ormas_kec/', views.jml_ormas_kec, name='jml_ormas_kec'),
    path('jml_ormas_kab/', views.jml_ormas_kab, name='jml_ormas_kab'),
]
