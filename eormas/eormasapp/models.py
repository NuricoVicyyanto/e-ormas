from django.db import models

# Create your models here.
class Desa(models.Model):
    desa = models.CharField(max_length=50)

    def __str__(self):
        return self.desa

class Kecamatan(models.Model):
    kecamatan = models.CharField(max_length=50)

    def __str__(self):
        return self.kecamatan

class Kabupaten(models.Model):
    kabupaten = models.CharField(max_length=50)

    def __str__(self):
        return self.kabupaten

class Unsur(models.Model):
    unsur = models.CharField(max_length=50)

    def __str__(self):
        return self.unsur

class Ormas(models.Model):
    nama = models.CharField(max_length=50)
    unsur = models.ForeignKey(Unsur, on_delete=models.CASCADE, null=True)
    alamat = models.CharField(max_length=50)
    desa = models.ForeignKey(Desa, on_delete=models.CASCADE, null=True)
    kecamatan = models.ForeignKey(Kecamatan, on_delete=models.CASCADE, null=True)
    kabupaten = models.ForeignKey(Kabupaten, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nama