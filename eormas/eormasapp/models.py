from django.db import models

# Create your models here.
class Desa(models.Model):
    desa = models.CharField(max_length=50)

    def __str__(self):
        return self.desa