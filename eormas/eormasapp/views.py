from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import os

# Create your views here.
def index(request):
    return render(request, 'backend/index.html')
def home(request):
    return render(request, 'backend/home.html')
def data_ormas(request):
    return render(request, 'backend/data_ormas.html')
def unsur_ormas(request):
    return render(request, 'backend/unsur_ormas.html')
def jml_ormas_ds(request):
    return render(request, 'backend/jml_ormas_ds.html')
def jml_ormas_kec(request):
    return render(request, 'backend/jml_ormas_kec.html')
def jml_ormas_kab(request):
    return render(request, 'backend/jml_ormas_kab.html')