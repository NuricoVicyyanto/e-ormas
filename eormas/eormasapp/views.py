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
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or password is incorrect')

    konteks = {}
    return render(request, 'backend/login.html', konteks)

@login_required(login_url='login')
def logout(request):
    auth_logout(request)
    return  redirect('dashboard')

@login_required(login_url='login')
def index(request):
    return render(request, 'backend/index.html')

@login_required(login_url='login')
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



@login_required(login_url='login')
def data_ormas(request):
    ormas = Ormas.objects.all()

    konteks ={
        'ormas':ormas,
    }

    return render(request, 'backend/data_ormas.html', konteks)

@login_required(login_url='login')
def hapus_ormas(request, id_ormas):
    ormas = Ormas.objects.get(id=id_ormas)
    ormas.delete()

    return redirect('data_ormas')

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
def jml_ormas_uns(request):
    ormas = Ormas.objects.values('unsur').annotate(
        jumlah=Count('unsur')
    ).order_by('unsur')

    konteks ={
                'ormas':ormas,
        }
    return render(request, 'backend/jml_ormas_uns.html', konteks)

@login_required(login_url='login')
def jml_ormas_ds(request):
    ormas = Ormas.objects.values('desa').annotate(
        jumlah=Count('desa')
    ).order_by('desa')

    konteks ={
                'ormas':ormas,
        }

    return render(request, 'backend/jml_ormas_ds.html', konteks)

@login_required(login_url='login')
def jml_ormas_kec(request):
    ormas = Ormas.objects.values('kecamatan').annotate(
        jumlah=Count('kecamatan')
    ).order_by('kecamatan')

    konteks ={
                'ormas':ormas,
        }
    return render(request, 'backend/jml_ormas_kec.html', konteks)

@login_required(login_url='login')
def jml_ormas_kab(request):
    ormas = Ormas.objects.values('kabupaten').annotate(
        jumlah=Count('kabupaten')
    ).order_by('kabupaten')

    konteks ={
                'ormas':ormas,
        }

    return render(request, 'backend/jml_ormas_kab.html', konteks)

@login_required(login_url='login')
def galeri(request):
    galeri = Galeri.objects.all()

    konteks = {
        'galeri' : galeri,
    }
    return render(request, 'backend/galeri.html', konteks)

@login_required(login_url='login')
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

@login_required(login_url='login')
def hapus_galeri(request, id_galeri):
    pohon = Galeri.objects.get(id=id_galeri)
    pohon.delete()

    return redirect('galeri')

@login_required(login_url='login')
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

@login_required(login_url='login')
def informasi(request):
    informasi = Informasi.objects.all()

    konteks ={
        'informasi':informasi,
    }
    return render(request, 'backend/informasi.html', konteks)

@login_required(login_url='login')
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

@login_required(login_url='login')
def hapus_informasi(request, id_informasi):
    informasi = Informasi.objects.get(id=id_informasi)
    informasi.delete()

    return redirect('informasi')

@login_required(login_url='login')
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