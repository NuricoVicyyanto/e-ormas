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

        JENIS =(
            ("Organisasi Masyarakat", "Organisasi Masyarakat"),
            ("Lembaga Swadaya Masyarakat(LSM)", "Lembaga Swadaya Masyarakat(LSM)"),
            ("Yayasan", "Yayasan"),
            ("Lainnya", "Lainnya"),
            )

        BIDANG =(
            ("Sosial", "Sosial"),
            ("Keagamaan", "Keagamaan"),
            ("Kebudayaan", "Kebudayaan"),
            ("Ekonomi", "Ekonomi"),
            ("Pendidikan", "Pendidikan"),
            ("Lainnya", "Lainnya"),
            )

        widgets = {
            'nama':forms.TextInput({'class':'form-control', 'id':'Nama'}),
            'unsur':forms.Select({'class':'form-control', 'id':'Unsur'}, choices=JENIS),
            'bidang':forms.Select({'class':'form-control', 'id':'Bidang'}, choices=BIDANG),
            'alamat':forms.TextInput({'class':'form-control', 'id':'Alamat'}),
            'desa':forms.TextInput({'class':'form-control', 'id':'Desa'}),
            'kecamatan':forms.TextInput({'class':'form-control', 'id':'Kecamatan'}),
            'kabupaten':forms.TextInput({'class':'form-control', 'id':'Kabupaten'}),
            'namaNotaris':forms.TextInput({'class':'form-control', 'id':'NamaNotaris'}),
            'noNotaris':forms.TextInput({'class':'form-control', 'id':'NoNotaris'}),
            'adArt':forms.TextInput({'class':'form-control', 'id':'AdArt'}),
            'sk':forms.TextInput({'class':'form-control', 'id':'SK'}),
            'masaBakti':forms.TextInput({'class':'form-control', 'id':'MasaBakti'}),
            'biodataKetua':forms.FileInput({'class':'form-control', 'id':'BiodataKetua'}),
            'biodataSekretaris':forms.FileInput({'class':'form-control', 'id':'BiodataSekretaris'}),
            'biodataBendahara':forms.FileInput({'class':'form-control', 'id':'BiodataBendahara'}),
            'status':forms.HiddenInput({'class':'form-control', 'id':'verifikasi'}), 
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


