from django.forms import ModelForm, widgets
from django import forms
from eormasapp.models import *

class FormDesa(ModelForm):
    class Meta:
        model = Desa
        fields = '__all__'
        #exclude = ['judul'] * untuk kolom yang tidak akan ditampilkan

        widgets = {
            'desa':forms.TextInput({'class':'form-control', 'id':'Desa'}),
        }