from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import CustomUser

@receiver(post_save, sender=CustomUser)
def user_create(sender, instance, created, **kwargs):
    if created:
        print(f"[SIGNAL]  User created: {instance.email}")
    else:
        print(f"[SIGNAL]  User updated: {instance.email}")
    
@receiver(post_delete, sender = CustomUser)
def user_delete(sender, instance, **kwargs):
    print(f"[SIGNAL]  User deleted: {instance.email}")