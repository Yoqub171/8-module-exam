from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Category
        fields = '__all__'