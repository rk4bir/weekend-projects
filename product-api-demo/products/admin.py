from django.contrib import admin
from .models import Size, Color, Price, Product


@admin.register(Size)
class SizeModelAdmin(admin.ModelAdmin):
    """Django admin functionality for Size Model"""
    list_per_page = 20
    list_display = ['id', 'title', 'description']
    list_display_links = ['title']
    list_filter = ['title']
    search_fields = ['title']


@admin.register(Color)
class ColorModelAdmin(admin.ModelAdmin):
    """Django admin functionality for Color Model"""
    list_per_page = 20
    list_display = ['id', 'title', 'color_code']
    list_display_links = ['title']
    list_filter = ['title']
    search_fields = ['title']


@admin.register(Price)
class PriceModelAdmin(admin.ModelAdmin):
    """Django admin functionality for Price Model"""
    list_per_page = 20
    list_display = ['id', 'price', 'start_date', 'end_date']
    list_display_links = ['price']
    list_filter = ['price', 'start_date', 'end_date']
    search_fields = ['price', 'start_date', 'end_date']


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    """Django admin functionality for Product Model"""
    list_per_page = 20
    list_display = ['pid', 'title', 'slug', 'in_stock', 'stocks']
    list_display_links = ['pid', 'title', 'slug']
    list_filter = ['title', 'pid', 'slug']
    search_fields = ['title', 'pid', 'slug']
