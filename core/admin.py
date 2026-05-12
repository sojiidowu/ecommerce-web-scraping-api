from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'query', 'name', 'price', 'link', 'image', 'created_at')
    search_fields = ('query', 'name', 'price')
    list_filter = ('query', 'created_at',)