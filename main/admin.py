from django.contrib import admin
from .models import Category, Items, Contacts
from django.utils.safestring import mark_safe


admin.site.register(Contacts)

@admin.register(Items)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo_img_tag', 'category', 'price', 'is_visible', 'sort')
    list_display_links = ('id', 'name',)
    list_editable = ('category', 'price', 'is_visible', 'sort')

    list_filter = ('category', 'is_visible',)
    search_fields = ('name',)

    def photo_img_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width='50px'>")


class ItemInline(admin.StackedInline):
    model = Items



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

    inlines = [ItemInline]