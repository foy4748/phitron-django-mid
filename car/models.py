from django.db import models
from django.utils import timezone


# Create your models here.
class Brand(models.Model):
    brand_name = models.CharField(max_length=1024)

    def __str__(self):
        return self.brand_name


class Car(models.Model):
    car_model = models.CharField(max_length=1024)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)

    car_image = models.ImageField(upload_to="car/uploads/", blank=True, null=True)
    description = models.TextField(max_length=5120)
    quantity = models.IntegerField()
    price = models.FloatField()
    createdAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.car_model
