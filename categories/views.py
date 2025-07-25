from rest_framework.viewsets import ModelViewSet
from .models import Category
from .serializers import CategorySerializer
from rest_framework.response import Response
from django.core.cache import cache

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        cache_key = 'category_list'
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data)

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        cache.set(cache_key, serializer.data, timeout=60)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        category_id = self.kwargs.get('pk')
        cache_key = f'category_detail_{category_id}'
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data)

        instance = self.get_object()
        serializer = self.get_serializer(instance)
        cache.set(cache_key, serializer.data, timeout=60)
        return Response(serializer.data)
