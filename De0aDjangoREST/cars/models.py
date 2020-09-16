from django.db import models


class Brand(models.Model):
    """
    Brand definition of cars
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=15)

