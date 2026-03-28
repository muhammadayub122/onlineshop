from django.shortcuts import render
from .models import Payment
from .serializer import PaymentSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer