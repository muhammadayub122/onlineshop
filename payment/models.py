from django.db import models

from order.models import Order

# Create your models here.

class Payment(models.Model):

    class Method(models.TextChoices):
        CASH= 'cash', 'Cash',
        CARD= 'card', 'Card',
        CLICK= 'click', 'Click',
        PAYME= 'payme', 'Payme',
    

    class Status(models.TextChoices):
         
        PENDING=  'pending', 'Pending',
        PROCESSING= 'processing', 'Processing',
        COMPLETED= 'completed', 'Completed',
        FAILED= 'failed', 'Failed',
        REFUNDED= 'refunded', 'Refunded',
        CANCELLED= 'cancelled', 'Cancelled',
 

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=20, choices=Method.choices)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)