from django.db import models

# Create your models here.
class User(models.Model):
    #pid = models.IntegerField(max_length=20)
    name = models.CharField(max_length=70)
    quantity = models.IntegerField(max_length=20)
    price = models.IntegerField(max_length=20)

