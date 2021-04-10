from django.contrib import admin
from .models import Product, Categories

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'categories',
        'price',
        'rating',
        'designer',
        'images',

    )

    ordering = ('sku',)


class CategoriesAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Categories, CategoriesAdmin)
