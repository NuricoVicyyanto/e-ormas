from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import os
from eormasapp.forms import FormDesa
from eormasapp.models import Desa

# Create your views here.
def index(request):
    return render(request, 'backend/index.html')

def home(request):
    return render(request, 'backend/home.html')

# desa
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


# kecamatan

def kecamatan(request):
    return render(request, 'backend/kecamatan.html')

# kabupaten
def kabupaten(request):
    return render(request, 'backend/kabupaten.html')

# data_ormas
def data_ormas(request):
    return render(request, 'backend/data_ormas.html')