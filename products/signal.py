from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Product

@receiver(post_save, sender=Product)
def product_created(sender, instance, created, **kwargs):
    if created:
        print(f"[SIGNAL]  Product created: {instance.name}")
    else:
        print(f"[SIGNAL]  Product uodated: {instance.name}")

    
@receiver(post_delete, sender=Product)
def product_delete(sender, instance, **kwargs):
    print(f"[SIGNAL]  Product deleted: {instance.name}")