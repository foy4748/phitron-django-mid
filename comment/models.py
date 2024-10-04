from django.db import models
from django.contrib.auth.models import User

# from django.utils import timezone

from car.models import Car

# Create your models here.


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    comment = models.TextField(max_length=2048)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
