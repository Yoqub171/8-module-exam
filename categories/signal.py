from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Category

@receiver(post_save, sender=Category)
def category_save(sender, instance, created, **kwargs):
    if created:
        print(f"[SIGNAL]   Category created: {instance.name}")
    else:
        print(f"[SIGNAL]   Category updated: {instance.name}")

@receiver(post_delete, sender=Category)
def category_delete(sender, instance, **kwargs):
        print(f"[SIGNAL]   Category deleted: {instance.name}")
