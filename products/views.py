from rest_framework.viewsets import ModelViewSet
from .models import Product, Category
from .serializers import ProductSerializer, ProductDetailSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models import Count
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.core.cache import cache
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


@method_decorator(cache_page(60), name='list')
class ProductViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description', 'category__name']
    filterset_fields = ['category', 'price', 'name']
    ordering_fields = ['price', 'created_at']
    ordering = ['-created_at']

    def get_queryset(self):
        return Product.objects.annotate(comments_count=Count('comments'))

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ProductDetailSerializer
        return ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        cache_key = f"product_detail_{pk}"
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data)

        instance = self.get_object()
        serializer = self.get_serializer(instance)
        cache.set(cache_key, serializer.data, timeout=60)
        return Response(serializer.data)
