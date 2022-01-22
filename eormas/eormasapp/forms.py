from django.forms import ModelForm, widgets
from django import forms
from eormasapp.models import *

class FormOrmas(ModelForm):
    class Meta:
        model = Ormas
        fields = '__all__'

        widgets = {
            'nama':forms.TextInput({'class':'form-control', 'id':'Nama'}),
            'unsur':forms.TextInput({'class':'form-control', 'id':'Unsur'}),
            'alamat':forms.TextInput({'class':'form-control', 'id':'Alamat'}),
            'desa':forms.TextInput({'class':'form-control', 'id':'Desa'}),
            'kecamatan':forms.TextInput({'class':'form-control', 'id':'Kecamatan'}),
            'kabupaten':forms.TextInput({'class':'form-control', 'id':'Kabupaten'}),
        }

class FormGaleri(ModelForm):
    class Meta:
        model = Galeri
        fields = '__all__'
        #exclude = ['judul'] * untuk kolom yang tidak akan ditampilkan

        widgets = {
            'image' : forms.FileInput({'class':'form-control'}),
            'judul':forms.TextInput({'class':'form-control', 'id':'Judul'}),
            'caption':forms.TextInput({'class':'form-control'}),
        }