# Generated by Django 3.2.11 on 2022-01-28 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eormasapp', '0011_informasi'),
    ]

    operations = [
        migrations.AddField(
            model_name='ormas',
            name='verifikasi',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
