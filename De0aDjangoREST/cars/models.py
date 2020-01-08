import uuid

from django.db import models


class Brand(models.Model):
    """
    Brand definition of cars
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=15)

    class Meta:
        ordering = ['name']


class Car(models.Model):
    """
    Car definition
    """
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    model = models.CharField(max_length=25)
    brand = models.ForeignKey(
        'Brand',
        related_name='cars',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['brand']
        indexes = [
            models.Index(fields=['brand'])
        ]
