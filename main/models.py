from ckeditor.fields import RichTextField
from django.db import models
from django.core.validators import RegexValidator

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(blank=True)
    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    class Meta:
        db_table = 'main_categories'
        ordering = ['sort', 'name']

    def __str__(self):
        return self.name


class Items(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    desc = models.TextField(max_length=500, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    photo = models.ImageField(upload_to='items/')
    sort = models.IntegerField(default=0)
    is_visible = models.BooleanField(default=True)

    class Meta:
        db_table = 'main_items'
        ordering = ('sort', 'name')

    def __str__(self):
        return self.name


class Contacts(models.Model):
    address = RichTextField()
    reservations = RichTextField()
    opening_hours = RichTextField()

    class Meta:
        db_table = 'main_contacts'
        ordering = ['id']








class Reservations(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?(38)?\d{10}$')

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, validators=[phone_regex])
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    number_guests = models.IntegerField()
    message = models.TextField(max_length=500)

    is_confirmed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'main_reservations'
        ordering = ('-date_created',)

    def __str__(self):
        return f"Reservation by {self.name} on {self.date} at {self.time}"


class Specials(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='specials/')
    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)




    def __str__(self):
        return self.title





