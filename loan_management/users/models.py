from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id_external = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255, blank=True)
    registry_code = models.CharField(max_length=14, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="adresses")
    street = models.CharField(max_length=255)
    number = models.IntegerField()
    complement = models.TextField(blank=True)
    zipcode = models.CharField(max_length=10)
    neighborhood = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
