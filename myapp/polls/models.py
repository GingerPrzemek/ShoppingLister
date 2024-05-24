from django.db import models

# Create your models here.
class Item(models.Model):

    id = models.BigAutoField(primary_key=True)
    itemName = models.CharField(max_length=200)
    qty = models.CharField(max_length=10)
    price = models.DecimalField(max_digits= 20, decimal_places=2, default= 0.00)
    def __str__(self):
        return self.itemName
