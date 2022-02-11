# Generated by Django 3.2.9 on 2022-02-10 23:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Galeri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='image/')),
                ('judul', models.CharField(max_length=50)),
                ('caption', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Informasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('informasi', models.CharField(max_length=50)),
                ('tanggal', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ormas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('unsur', models.CharField(max_length=50)),
                ('bidang', models.CharField(max_length=50)),
                ('alamat', models.CharField(max_length=50)),
                ('buktiAlamat', models.FileField(null=True, upload_to='image/')),
                ('desa', models.CharField(max_length=50)),
                ('kecamatan', models.CharField(max_length=50)),
                ('kabupaten', models.CharField(max_length=50)),
                ('namaNotaris', models.CharField(max_length=50)),
                ('noNotaris', models.CharField(max_length=50)),
                ('skTerdaftar', models.FileField(null=True, upload_to='image/')),
                ('skPengurus', models.FileField(null=True, upload_to='image/')),
                ('namaKetua', models.CharField(max_length=50)),
                ('ttlKetua', models.CharField(max_length=50)),
                ('noKetua', models.CharField(max_length=50)),
                ('biodataKetua', models.FileField(null=True, upload_to='image/')),
                ('namaSekretaris', models.CharField(max_length=50)),
                ('ttlSekretaris', models.CharField(max_length=50)),
                ('noSekretaris', models.CharField(max_length=50)),
                ('biodataSekretaris', models.FileField(null=True, upload_to='image/')),
                ('namaBendahara', models.CharField(max_length=50)),
                ('ttlBendahara', models.CharField(max_length=50)),
                ('noBendahara', models.CharField(max_length=50)),
                ('biodataBendahara', models.FileField(null=True, upload_to='image/')),
                ('status', models.CharField(default='0', max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ormas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
