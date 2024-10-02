from django.db import models


# Create your models here.
class Brand(models.Model):
    brand_name = models.CharField(max_length=1024)

    def __str__(self):
        return self.brand_name


class Car(models.Model):
    car_model = models.CharField(max_length=1024)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.car_model
