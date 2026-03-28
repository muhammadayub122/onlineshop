from django.db import models
from django.contrib.auth.models import AbstractUser



    

  

class User(AbstractUser):
    class Role(models.TextChoices):
        SELLER = 'seller', 'Seller'
        USER = 'user', 'User'
        ADMIN = 'admin', 'Admin'

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13)
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.USER)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)