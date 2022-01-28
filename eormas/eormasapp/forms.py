from django.forms import CheckboxInput, ModelForm, widgets
from django import forms
from eormasapp.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
                'username':forms.TextInput({'class':'form-control', 'id':'Username'}),
                'image' : forms.FileInput({'class':'form-control'}),
                'informasi':forms.TextInput({'class':'form-control'}),
            }

class FormOrmas(ModelForm):
    class Meta:
        model = Ormas
        fields = '__all__'
        # exclude = ['action']

        widgets = {
            'nama':forms.TextInput({'class':'form-control', 'id':'Nama',}),
            'unsur':forms.TextInput({'class':'form-control', 'id':'Unsur'}),
            'alamat':forms.TextInput({'class':'form-control', 'id':'Alamat'}),
            'desa':forms.TextInput({'class':'form-control', 'id':'Desa'}),
            'kecamatan':forms.TextInput({'class':'form-control', 'id':'Kecamatan'}), 
<<<<<<< Updated upstream
<<<<<<< Updated upstream
            'kabupaten':forms.TextInput({'class':'form-control', 'id':'Kabupaten'}), 
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
            'verifikasi':forms.HiddenInput({'class':'form-control', 'id':'verifikasi'}), 
        }
        
class VerFormOrmas(ModelForm):
    class Meta:
        model = Ormas
        fields = '__all__'

        widgets = {
            'verifikasi' : CheckboxInput(attrs={'class': 'required checkbox form-control'}),   
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

class FormInformasi(ModelForm):
    class Meta:
        model = Informasi
        fields = '__all__'
        #exclude = ['judul'] * untuk kolom yang tidak akan ditampilkan

        widgets = {
            'informasi' : forms.TextInput({'class':'form-control'}),
            'tanggal':forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'type':'date'}),
        }