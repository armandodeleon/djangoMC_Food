from django.db import models


# Create your models here.

class Item(models.Model):

    def __str__(self):  # object representation
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=200)
    item_price = models.DecimalField(max_digits=4, decimal_places=2)

