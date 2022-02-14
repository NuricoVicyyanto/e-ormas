from django.forms import CheckboxInput, ModelForm, widgets
from django import forms
from eormasapp.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput({'class': 'form-control', 'id': 'Username'}),
            'image': forms.FileInput({'class': 'form-control'}),
            'informasi': forms.TextInput({'class': 'form-control'}),
        }


class FormUser(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Username', 'class': 'form-control', }))
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'form-control', 'data-toggle': 'password', 'id': 'password', 'name': 'password', }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class FormOrmas(ModelForm):
    class Meta:
        model = Ormas
        fields = '__all__'

        JENIS = (
            ("Organisasi Masyarakat", "Organisasi Masyarakat"),
            ("Lembaga Swadaya Masyarakat(LSM)", "Lembaga Swadaya Masyarakat(LSM)"),
            ("Yayasan", "Yayasan"),
            ("Lainnya", "Lainnya"),
        )

        BIDANG = (
            ("Sosial", "Sosial"),
            ("Keagamaan", "Keagamaan"),
            ("Kebudayaan", "Kebudayaan"),
            ("Ekonomi", "Ekonomi"),
            ("Pendidikan", "Pendidikan"),
            ("Lainnya", "Lainnya"),
        )

        widgets = {
            'user': forms.HiddenInput(),
            'nama': forms.TextInput({'class': 'form-control', 'id': 'Nama'}),
            'unsur': forms.Select({'class': 'form-control', 'id': 'Unsur'}, choices=JENIS),
            'bidang': forms.Select({'class': 'form-control', 'id': 'Bidang'}, choices=BIDANG),
            'alamat': forms.TextInput({'class': 'form-control', 'id': 'Alamat'}),
            'buktiAlamat': forms.FileInput({'class': 'form-control-file', 'id': 'BuktiAlamat'}),
            'desa': forms.TextInput({'class': 'form-control', 'id': 'Desa'}),
            'kecamatan': forms.TextInput({'class': 'form-control', 'id': 'Kecamatan'}),
            'kabupaten': forms.TextInput({'class': 'form-control', 'id': 'Kabupaten'}),
            'namaNotaris': forms.TextInput({'class': 'form-control', 'id': 'NamaNotaris'}),
            'noNotaris': forms.TextInput({'class': 'form-control', 'id': 'NoNotaris'}),
            'skTerdaftar': forms.FileInput({'class': 'form-control-file', 'id': 'SkTerdaftar'}),
            'skPengurus': forms.FileInput({'class': 'form-control-file', 'id': 'SkPengurus'}),

            'namaKetua': forms.TextInput({'class': 'form-control', 'id': 'NamaKetua'}),
            'ttlKetua': forms.TextInput({'class': 'form-control', 'id': 'TtlKetua'}),
            'noKetua': forms.TextInput({'class': 'form-control', 'id': 'NoKetua'}),
            'biodataKetua': forms.FileInput({'class': 'form-control-file', 'id': 'BiodataKetua'}),

            'namaSekretaris': forms.TextInput({'class': 'form-control', 'id': 'NamaSekretaris'}),
            'ttlSekretaris': forms.TextInput({'class': 'form-control', 'id': 'TtlSekretaris'}),
            'noSekretaris': forms.TextInput({'class': 'form-control', 'id': 'NoSekretaris'}),
            'biodataSekretaris': forms.FileInput({'class': 'form-control-file', 'id': 'BiodataSekretaris'}),

            'namaBendahara': forms.TextInput({'class': 'form-control', 'id': 'NamaBendahara'}),
            'ttlBendahara': forms.TextInput({'class': 'form-control', 'id': 'TtlBendahara'}),
            'noBendahara': forms.TextInput({'class': 'form-control', 'id': 'NoBendahara'}),
            'biodataBendahara': forms.FileInput({'class': 'form-control-file', 'id': 'BiodataBendahara'}),

            'status': forms.HiddenInput({'class': 'form-control', 'id': 'verifikasi'}),
        }


class FormGaleri(ModelForm):
    class Meta:
        model = Galeri
        fields = '__all__'
        # exclude = ['judul'] * untuk kolom yang tidak akan ditampilkan

        widgets = {
            'image': forms.FileInput({'class': 'form-control'}),
            'judul': forms.TextInput({'class': 'form-control', 'id': 'Judul'}),
            'caption': forms.TextInput({'class': 'form-control'}),
        }


class FormInformasi(ModelForm):
    class Meta:
        model = Informasi
        fields = '__all__'
        # exclude = ['judul'] * untuk kolom yang tidak akan ditampilkan

        widgets = {
            'informasi': forms.TextInput({'class': 'form-control'}),
            'tanggal': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'form-control', 'type': 'date'}),
        }
