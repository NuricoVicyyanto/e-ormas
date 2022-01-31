from django.db import models
from django.conf import settings

# Create your models here.


class Ormas(models.Model):

    nama = models.CharField(max_length=50)
    unsur = models.CharField(max_length=50)
    alamat = models.CharField(max_length=50)
    desa = models.CharField(max_length=50)
    kecamatan = models.CharField(max_length=50)
    kabupaten = models.CharField(max_length=50)
    status = models.CharField(max_length=1, default="0")
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nama

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
    
    
    
