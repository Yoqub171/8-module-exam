from django.core.cache import cache
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['text', 'product__name', 'user__email']
    filterset_fields = ['product', 'user']
    ordering_fields = ['created_at', 'id']
    ordering = ['-created_at']

    def get_queryset(self):
        key = 'comments_queryset'
        qs = cache.get(key)
        if qs:
            return qs
        qs = Comment.objects.select_related('product', 'user').all()
        cache.set(key, qs, timeout=60)
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        cache.delete('comments_queryset')

    def perform_update(self, serializer):
        serializer.save()
        cache.delete('comments_queryset')

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.check_object_permissions(request, instance)
        self.perform_destroy(instance)
        cache.delete('comments_queryset')
        return Response(status=status.HTTP_204_NO_CONTENT)


    def get_serializer_class(self):
        if self.action == "retrieve":
            return CommentDetailSerializer
        return CommentSerializer

    def retrieve(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        cache_key = f'comment_detail_{pk}'
        cached = cache.get(cache_key)
        if cached:
            return Response(cached)

        instance = self.get_object()
        serializer = self.get_serializer(instance)
        cache.set(cache_key, serializer.data, timeout=60)
        return Response(serializer.data)
