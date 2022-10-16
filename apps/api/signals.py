from .models import Advocate, Link
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=Advocate)
def create_advocate_link(sender, instance, created, **kwargs):
    if created:
        Link.objects.create(advocate=instance)
