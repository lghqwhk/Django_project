# Generated by Django 4.2.20 on 2025-04-28 15:37

import ckeditor.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=500)),
                ('photo', models.ImageField(upload_to='news/')),
                ('date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='contacts',
            name='address',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='opening_hours',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='reservations',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='reservations',
            name='phone',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(regex='^\\+?(38)?\\d{10}$')]),
        ),
    ]
