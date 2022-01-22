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