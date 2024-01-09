from django.db import models


# Create your models here.

class Item(models.Model):

    def __str__(self):  # object representation
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=200)
    item_price = models.DecimalField(max_digits=4, decimal_places=2)
    item_image = models.CharField(max_length=500, default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfdIv7mYroRcEro01QihNy4FertDfXFWtetQ&usqp=CAU')
