# Generated by Django 3.2.9 on 2022-01-28 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eormasapp', '0025_alter_ormas_verifikasi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ormas',
            name='verifikasi',
        ),
    ]
