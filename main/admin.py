from django.contrib import admin
from .models import Category , Items



admin.site.register(Items)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
