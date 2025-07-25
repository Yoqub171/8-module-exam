from django.db import models
from django.conf import settings
from products.models import Product
from django.core.validators import MinValueValidator, MaxValueValidator

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    rating = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateField(auto_now_add=True)    

    def __str__(self):
        return f"{self.user.email} - {self.product.name}"
    
class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='likes')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'comment']

    def __str__(self):
        return f"{self.user.email} liked comment {self.comment.id}"
