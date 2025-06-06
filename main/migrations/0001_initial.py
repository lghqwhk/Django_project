# Generated by Django 4.2.20 on 2025-04-18 08:46

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('sort', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'main_categories',
                'ordering': ['sort', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', ckeditor.fields.RichTextField(max_length=500)),
                ('reservations', ckeditor.fields.RichTextField(max_length=500)),
                ('opening_hours', ckeditor.fields.RichTextField(max_length=500)),
            ],
            options={
                'db_table': 'main_contacts',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('number_guests', models.IntegerField()),
                ('message', models.TextField(max_length=500)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'main_reservations',
                'ordering': ('-date_created',),
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('desc', models.TextField(max_length=500, unique=True)),
                ('photo', models.ImageField(upload_to='items/')),
                ('sort', models.IntegerField(default=0)),
                ('is_visible', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='main.category')),
            ],
            options={
                'db_table': 'main_items',
                'ordering': ('sort', 'name'),
            },
        ),
    ]
