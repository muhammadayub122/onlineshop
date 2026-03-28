from django.shortcuts import render
from .models import Order, OrderItem
from .serializer import OrderSerializer, OrderItemSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.
class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
