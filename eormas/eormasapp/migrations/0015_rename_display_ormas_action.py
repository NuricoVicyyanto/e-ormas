# Generated by Django 3.2.9 on 2022-01-28 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eormasapp', '0014_auto_20220128_1214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ormas',
            old_name='display',
            new_name='action',
        ),
    ]
