
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100 , unique=True)
    slug = models.SlugField( blank=True)
    is_visible = models.BooleanField(default=True )
    sort = models.IntegerField(default=0)


    class Meta:
        db_table = 'main_categories'
        ordering = ['sort', 'name']

    def __str__(self):
        return self.name
    verbose_name='Item'
    verbose_name_plural='Items'

    def __iter__(self):
        for item in self.items.filter(is_visible=True):
            yield item

class Items(models.Model):
    name = models.CharField(max_length=100 , unique=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    desc = models.TextField(max_length=500 , unique = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE , related_name='items')
    photo = models.ImageField(upload_to='items/')



    class Meta:
        db_table = 'main_items'
        ordering = ('sort', 'name')

    def __str__(self):
        return self.name

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)
