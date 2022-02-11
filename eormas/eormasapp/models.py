from django import forms
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


class Ormas(models.Model):
    user = models.OneToOneField(User, related_name='ormas', on_delete=models.CASCADE)
    nama = models.CharField(max_length=50)
    unsur = models.CharField(max_length=50) # Jenis
    bidang = models.CharField(max_length=50)
    alamat = models.CharField(max_length=50)
    buktiAlamat = models.FileField(upload_to='image/', null=True)
    desa = models.CharField(max_length=50) #Kelurahan
    kecamatan = models.CharField(max_length=50)
    kabupaten = models.CharField(max_length=50)
    namaNotaris = models.CharField(max_length=50)
    noNotaris = models.CharField(max_length=50)
    skTerdaftar = models.FileField(upload_to='image/', null=True)
    skPengurus = models.FileField(upload_to='image/', null=True)
    
    #biodata ketua
    namaKetua = models.CharField(max_length=50)
    ttlKetua = models.CharField(max_length=50)
    noKetua = models.CharField(max_length=50)
    biodataKetua = models.FileField(upload_to='image/', null = True)

    #biodata sekretaris
    namaSekretaris = models.CharField(max_length=50)
    ttlSekretaris = models.CharField(max_length=50)
    noSekretaris = models.CharField(max_length=50)
    biodataSekretaris = models.FileField(upload_to='image/', null = True)


    #biodataBendahara
    namaBendahara = models.CharField(max_length=50)
    ttlBendahara = models.CharField(max_length=50)
    noBendahara = models.CharField(max_length=50)
    biodataBendahara = models.FileField(upload_to='image/', null = True)

    status = models.CharField(max_length=1, default="0")

    def __str__(self):
        return self.user.username

    def clean(self):
        self.unsur = self.unsur.capitalize()
        self.desa = self.desa.upper()
        self.kecamatan = self.kecamatan.upper()
        self.kabupaten = self.kabupaten.upper()

class Galeri(models.Model):
    image = models.ImageField(upload_to='image/', null = True)
    judul = models.CharField(max_length=50)
    caption = models.TextField()

    def __str__(self):
        return self.judul

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

class Informasi(models.Model):
    informasi = models.CharField(max_length=50)
    tanggal = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.informasi