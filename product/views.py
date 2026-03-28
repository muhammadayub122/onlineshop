from django.shortcuts import render
from .models import ProductCategory, Product
from .serializer import ProductCategorySerializer, ProductSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class ProductCategoryViewSet(ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer