from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import os

# Create your views here.
def home(request):
    return render(request, 'backend/home.html')