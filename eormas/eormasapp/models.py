from django.db import models

# Create your models here.

class Ormas(models.Model):
    nama = models.CharField(max_length=50)
    unsur = models.CharField(max_length=50)
    alamat = models.CharField(max_length=50)
    desa = models.CharField(max_length=50)
    kecamatan = models.CharField(max_length=50)
    kabupaten = models.CharField(max_length=50)

    def __str__(self):
        return self.nama

    def clean(self):
        self.unsur = self.unsur.capitalize()
        self.desa = self.desa.upper()
        self.kecamatan = self.kecamatan.upper()
        self.kabupaten = self.kabupaten.upper()