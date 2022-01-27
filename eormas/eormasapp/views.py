from collections import Counter
from django.db.models import Count
from itertools import count
from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import os
from eormasapp.forms import *
from eormasapp.models import *

# Create your views here.
def index(request):
    return render(request, 'backend/index.html')

def landing(request):
    return render(request, 'backend/landing.html')

def dashboard(request):
    return render(request, 'frontend/home.html')

def ormas(request):
    ormas = Ormas.objects.all()

    konteks ={
        'ormas':ormas,
    }

    return render(request, 'frontend/ormas.html', konteks)

def ormas_uns(request):
    ormas = Ormas.objects.values('unsur').annotate(
        jumlah=Count('unsur')
    ).order_by('unsur')

    konteks ={
                'ormas':ormas,
        }
    return render(request, 'frontend/ormas_uns.html', konteks)

def ormas_ds(request):
    ormas = Ormas.objects.values('desa').annotate(
        jumlah=Count('desa')
    ).order_by('desa')

    konteks ={
                'ormas':ormas,
        }

    return render(request, 'frontend/ormas_ds.html', konteks)

def ormas_kec(request):
    ormas = Ormas.objects.values('kecamatan').annotate(
        jumlah=Count('kecamatan')
    ).order_by('kecamatan')

    konteks ={
                'ormas':ormas,
        }
    return render(request, 'frontend/ormas_kec.html', konteks)

def ormas_kab(request):
    ormas = Ormas.objects.values('kabupaten').annotate(
        jumlah=Count('kabupaten')
    ).order_by('kabupaten')

    konteks ={
                'ormas':ormas,
        }

    return render(request, 'frontend/ormas_kab.html', konteks)

def grafik(request):
    desa = Ormas.objects.values('desa').annotate(
        jumlah=Count('desa')
    ).order_by('desa')
    kecamatan = Ormas.objects.values('kecamatan').annotate(
        jumlah=Count('kecamatan')
    ).order_by('kecamatan')

    konteks ={
                'desa':desa,
                'kecamatan':kecamatan,
        }

    return render(request, 'frontend/grafik.html', konteks)

def galeri_view(request):
    galeri = Galeri.objects.all()

    konteks = {
        'galeri' : galeri,
    }
    return render(request, 'frontend/galeri.html', konteks)




def data_ormas(request):
    ormas = Ormas.objects.all()

    konteks ={
        'ormas':ormas,
    }

    return render(request, 'backend/data_ormas.html', konteks)

def hapus_ormas(request, id_ormas):
    ormas = Ormas.objects.get(id=id_ormas)
    ormas.delete()

    return redirect('data_ormas')

def tambah_ormas(request):
    if request.POST:
        form = FormOrmas(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            alert = 'Data Berhasil Ditambahkan'
            form = FormOrmas

            konteks={
                'form':form,
                'alert':alert,
            }

            return render(request, 'backend/add_data_ormas.html', konteks)

    else:
        form = FormOrmas()

        konteks ={
            'form':form,
        }

    return render(request, 'backend/add_data_ormas.html', konteks)

def edit_ormas(request, id_ormas):
    data_ormas = Ormas.objects.get(id=id_ormas)
    template = 'backend/edit_data_ormas.html'
    if request.POST:
        form = FormOrmas(request.POST,request.FILES, instance=data_ormas)
        if form.is_valid():
            form.save()
            return redirect('edit_ormas', id_ormas=id_ormas)
    else:
        form = FormOrmas(instance=data_ormas)
        konteks ={
            'form':form,
            'data_ormas':data_ormas,
        }
        return render(request, template, konteks)

def jml_ormas_uns(request):
    ormas = Ormas.objects.values('unsur').annotate(
        jumlah=Count('unsur')
    ).order_by('unsur')

    konteks ={
                'ormas':ormas,
        }
    return render(request, 'backend/jml_ormas_uns.html', konteks)

def jml_ormas_ds(request):
    ormas = Ormas.objects.values('desa').annotate(
        jumlah=Count('desa')
    ).order_by('desa')

    konteks ={
                'ormas':ormas,
        }

    return render(request, 'backend/jml_ormas_ds.html', konteks)

def jml_ormas_kec(request):
    ormas = Ormas.objects.values('kecamatan').annotate(
        jumlah=Count('kecamatan')
    ).order_by('kecamatan')

    konteks ={
                'ormas':ormas,
        }
    return render(request, 'backend/jml_ormas_kec.html', konteks)

def jml_ormas_kab(request):
    ormas = Ormas.objects.values('kabupaten').annotate(
        jumlah=Count('kabupaten')
    ).order_by('kabupaten')

    konteks ={
                'ormas':ormas,
        }

    return render(request, 'backend/jml_ormas_kab.html', konteks)


def galeri(request):
    galeri = Galeri.objects.all()

    konteks = {
        'galeri' : galeri,
    }
    return render(request, 'backend/galeri.html', konteks)


def tambah_galeri(request):
    if request.POST:
        form = FormGaleri(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            alert = 'Data Berhasil Ditambahkan'
            form = FormGaleri

            konteks={
                'form':form,
                'alert':alert,
            }

            return render(request, 'backend/tambah_galeri.html', konteks)

    else:
        form = FormGaleri()

        konteks ={
            'form':form,
        }

    return render(request, 'backend/tambah_galeri.html', konteks)


def hapus_galeri(request, id_galeri):
    pohon = Galeri.objects.get(id=id_galeri)
    pohon.delete()

    return redirect('galeri')


def edit_galeri(request, id_galeri):
    galeri = Galeri.objects.get(id=id_galeri)
    template = 'backend/edit_galeri.html'
    if request.POST:
        form = FormGaleri(request.POST,request.FILES, instance=galeri)
        if form.is_valid():
            form.save()
            return redirect('galeri')
    else:
        form = FormGaleri(instance=galeri)
        konteks ={
            'form':form,
            'galeri':galeri,
        }
        return render(request, template, konteks)

def informasi(request):
    informasi = Informasi.objects.all()

    konteks ={
        'informasi':informasi,
    }
    return render(request, 'backend/informasi.html', konteks)

def tambah_informasi(request):
    if request.POST:
        form = FormInformasi(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            alert = 'Data Berhasil Ditambahkan'
            form = FormInformasi

            konteks={
                'form':form,
                'alert':alert,
            }

            return render(request, 'backend/tambah_informasi.html', konteks)

    else:
        form = FormInformasi()

        konteks ={
            'form':form,
        }

    return render(request, 'backend/tambah_informasi.html', konteks)

def hapus_informasi(request, id_informasi):
    informasi = Informasi.objects.get(id=id_informasi)
    informasi.delete()

    return redirect('informasi')

def edit_informasi(request, id_informasi):
    informasi = Informasi.objects.get(id=id_informasi)
    template = 'backend/edit_informasi.html'
    if request.POST:
        form = FormInformasi(request.POST,request.FILES, instance=informasi)
        if form.is_valid():
            form.save()
            return redirect('informasi')
    else:
        form = FormInformasi(instance=informasi)
        konteks ={
            'form':form,
            'informasi':informasi,
        }
        return render(request, template, konteks)