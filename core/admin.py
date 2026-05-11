from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'link', 'image', 'created_at')
    search_fields = ('name', 'price')
    list_filter = ('created_at',)