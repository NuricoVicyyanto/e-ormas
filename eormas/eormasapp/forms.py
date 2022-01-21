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

class FormKecamatan(ModelForm):
    class Meta:
        model = Kecamatan
        fields = '__all__'

        widgets = {
            'kecamatan':forms.TextInput({'class':'form-control', 'id':'Kecamatan'})
        }

class FormKabupaten(ModelForm):
    class Meta:
        model = Kabupaten
        fields = '__all__'

        widgets = {
            'kabupaten':forms.TextInput({'class':'form-control', 'id':'Kabupaten'})
        }

class FormUnsur(ModelForm):
    class Meta:
        model = Unsur
        fields = '__all__'

        widgets = {
            'unsur':forms.TextInput({'class':'form-control', 'id':'Unsur'})
        }

class FormOrmas(ModelForm):
    class Meta:
        model = Ormas
        fields = '__all__'

        widgets = {
            'nama':forms.TextInput({'class':'form-control', 'id':'Nama'}),
            'unsur':forms.Select({'class':'form-control', 'id':'Unsur'}),
            'alamat':forms.TextInput({'class':'form-control', 'id':'Alamat'}),
            'desa':forms.Select({'class':'form-control', 'id':'Desa'}),
            'kecamatan':forms.Select({'class':'form-control', 'id':'Kecamatan'}),
            'kabupaten':forms.Select({'class':'form-control', 'id':'Kabupaten'})
        }