# Generated by Django 4.0.1 on 2022-01-27 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eormasapp', '0010_galeri'),
    ]

    operations = [
        migrations.CreateModel(
            name='Informasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('informasi', models.CharField(max_length=50)),
                ('tanggal', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
