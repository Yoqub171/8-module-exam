from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Comment
from django.core.cache import cache

@receiver(post_save, sender=Comment)
def clear_cache_on_comment_save(sender, instance, created, **kwargs):
    print("[SIGNAL]  Comment saved or updated")
    cache.clear()

@receiver(post_delete, sender=Comment)
def clear_cache_on_comment_delete(sender, instance, **kwargs):
    print("[SIGNAL]  Comment deleted")
    cache.clear()
