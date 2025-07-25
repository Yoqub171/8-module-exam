from rest_framework import serializers
from .models import Category, Product
from comments.serializers import CommentSerializer
from categories.serializers import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['id', 'created_at']

class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    comments = CommentSerializer(source='comment_set', many=True, read_only=True)
    comments_count = serializers.SerializerMethodField()
    image = serializers.ImageField(use_url=True)


    class Meta:
        model = Product
        fields = '__all__'

    def get_comments_count(self, obj):
        return obj.comments_count
