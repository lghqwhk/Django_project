
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    is_visible = models.BooleanField(default=True , unique=True)
    sort = models.IntegerField(default=0)


    class Meta:
        db_table = 'main_categories'
        ordering = ['sort', 'name']

    def __str__(self):
        return self.name

class Items(models.Model):
    name = models.CharField(max_length=100 , unique=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    desc = models.TextField(max_length=500 , unique = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='items/')



    class Meta:
        db_table = 'main_items'

    is_visible= models.BooleanField(default=True)
    sort = models.IntegerField(default=0)
