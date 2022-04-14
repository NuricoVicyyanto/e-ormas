from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Ormas
from django.core.exceptions import ObjectDoesNotExist


@receiver(post_save, sender=User)
def create_ormas(sender, instance, created, **kwargs):
    try:
        instance.ormas.save()
    except ObjectDoesNotExist:
        Ormas.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_ormas(sender, instance, **kwargs):
    instance.ormas.save()
