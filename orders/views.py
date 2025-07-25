from rest_framework.viewsets import ModelViewSet
from .models import Order
from .serializers import OrderSerializer, OrderDetailSerializer
from rest_framework.permissions import IsAuthenticated

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return OrderDetailSerializer
        return OrderSerializer
    