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

def desa(request):
    desa = Desa.objects.all()

    konteks ={
        'desa':desa,
    }

    return render(request, 'backend/desa.html', konteks)

def tambah_desa(request):
    if request.POST:
        form = FormDesa(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            alert = 'Data Berhasil Ditambahkan'
            form = FormDesa

            konteks={
                'form':form,
                'alert':alert,
            }

            return render(request, 'backend/tambah_desa.html', konteks)

    else:
        form = FormDesa()

        konteks ={
            'form':form,
        }

    return render(request, 'backend/tambah_desa.html', konteks)

def edit_desa(request, id_desa):
    desa = Desa.objects.get(id=id_desa)
    template = 'backend/edit_desa.html'
    if request.POST:
        form = FormDesa(request.POST,request.FILES, instance=desa)
        if form.is_valid():
            form.save()
            return redirect('edit_desa', id_desa=id_desa)
    else:
        form = FormDesa(instance=desa)
        konteks ={
            'form':form,
            'desa':desa,
        }
        return render(request, template, konteks)


def hapus_desa(request, id_desa):
    desa = Desa.objects.get(id=id_desa)
    desa.delete()

    return redirect('desa')

def kecamatan(request):
    kecamatan = Kecamatan.objects.all()

    konteks ={
        'kecamatan':kecamatan,
    }

    return render(request, 'backend/kecamatan.html', konteks)

def hapus_kecamatan(request, id_kecamatan):
    kecamatan = Kecamatan.objects.get(id=id_kecamatan)
    kecamatan.delete()

    return redirect('kecamatan')

def tambah_kecamatan(request):
    if request.POST:
        form = FormKecamatan(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            alert = 'Data Berhasil Ditambahkan'
            form = FormKecamatan

            konteks={
                'form':form,
                'alert':alert,
            }

            return render(request, 'backend/tambah_kecamatan.html', konteks)

    else:
        form = FormKecamatan()

        konteks ={
            'form':form,
        }

    return render(request, 'backend/tambah_kecamatan.html', konteks)

def kabupaten(request):
    kabupaten = Kabupaten.objects.all()

    konteks ={
        'kabupaten':kabupaten,
    }

    return render(request, 'backend/kabupaten.html', konteks)

def hapus_kabupaten(request, id_kabupaten):
    kabupaten = Kabupaten.objects.get(id=id_kabupaten)
    kabupaten.delete()

    return redirect('kabupaten')

def tambah_kabupaten(request):
    if request.POST:
        form = FormKabupaten(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            alert = 'Data Berhasil Ditambahkan'
            form = FormKabupaten

            konteks={
                'form':form,
                'alert':alert,
            }

            return render(request, 'backend/tambah_kabupaten.html', konteks)

    else:
        form = FormKabupaten()

        konteks ={
            'form':form,
        }

    return render(request, 'backend/tambah_kabupaten.html', konteks)

    
def data_ormas(request):
    ormas = Ormas.objects.all()

    konteks ={
        'ormas':ormas,
    }

    return render(request, 'backend/data_ormas.html', konteks)

def hapus_ormas(request, id_ormas):
    ormas = Ormas.objects.get(id=id_ormas)
    ormas.delete()

    return redirect('ormas')

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

def unsur(request):
    unsur = Unsur.objects.all()

    konteks ={
        'unsur':unsur,
    }

    return render(request, 'backend/unsur_ormas.html', konteks)

def tambah_unsur(request):
    if request.POST:
        form = FormUnsur(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            alert = 'Data Berhasil Ditambahkan'
            form = FormUnsur

            konteks={
                'form':form,
                'alert':alert,
            }

            return render(request, 'backend/tambah_unsur.html', konteks)

    else:
        form = FormUnsur()

        konteks ={
            'form':form,
        }

    return render(request, 'backend/tambah_unsur.html', konteks)

def unsur_ormas(request):
    return render(request, 'backend/unsur_ormas.html')
def jml_ormas_ds(request):
    return render(request, 'backend/jml_ormas_ds.html')
def jml_ormas_kec(request):
    return render(request, 'backend/jml_ormas_kec.html')
def jml_ormas_kab(request):
    return render(request, 'backend/jml_ormas_kab.html')
def galeri(request):
    return render(request, 'backend/galeri.html')