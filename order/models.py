from django.db import models

from product.models import Product
from user.models import User

# Create your models here.
class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        AWAITING_PAYMENT = 'awaiting_payment', 'Awaiting Payment'
        PROCESSING = 'processing', 'Processing'
        SHIPPED = 'shipped', 'Shipped'
        IN_TRANSIT = 'in_transit', 'In Transit'
        DELIVERED = 'delivered', 'Delivered'
        COMPLETED = 'completed', 'Completed'
        CANCELLED = 'cancelled', 'Cancelled'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
