from django.db import models

# Create your models here.
class Item(models.Model):
    id = models.IntegerField(default=1)
    itemName = models.CharField(max_length=200)
    qty = models.CharField(max_length=10)
