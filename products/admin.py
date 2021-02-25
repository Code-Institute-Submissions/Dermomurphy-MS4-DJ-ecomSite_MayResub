from django.contrib import admin
from .models import Product, Brewery
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'ibu',
        'abv',
        'brewery',
        'price',
        'rating',
        'image',
    )
    
    ordering = ('name',)

class BreweryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'country',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Brewery, BreweryAdmin)