from rest_framework import serializers
from .models import Comment
from products.models import Product
from users.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.email')
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = Comment 
        fields = '__all__'
        read_only_fields = ['id', 'owner', 'created_at']


class CommentDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    product = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = '__all__'

    def get_product(self, obj):
        from products.serializers import ProductSerializer
        return ProductSerializer(obj.product).data

