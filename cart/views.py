from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Cart, CartItem
from .serializer import CartSerializer, CartItemSerializer
# Create your views here.
class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer   
class CartItemViewSet(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer