from django.db import models
from model_utils.models import TimeStampedModel


class Bank(TimeStampedModel):
    name = models.CharField(max_length=255)
    tax_identification = models.CharField(max_length=255)
