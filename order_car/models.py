from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from car.models import Car

# Create your models here.


class CarOrder(models.Model):
    buyer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=timezone.now)
