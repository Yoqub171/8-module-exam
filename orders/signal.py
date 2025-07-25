from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from .models import Order

@receiver(post_save, sender=Order)
def order_save(sender, instance, created, **kwargs):
    if created:
        print(f"[SIGNAL]  Order created: {instance.id}")
    else:
        print(f"[SIGNAL]  Order updated: {instance.id}")

@receiver(post_delete, sender=Order)
def order_delete(sender, instance, **kwargs):
    print(f"[SIGNAL]  Order deleted: {instance.id}")