from django.db import models

# Create your models here.


class Address(models.Model):
    street = models.TextField(blank=True)
    number = models.IntegerField(blank=True)