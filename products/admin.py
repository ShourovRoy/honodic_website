from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_filter = ["title", "is_featured"]
    ordering = ["updated_at"]
    search_fields = ["is_featured"]
    list_display = ["title", "is_featured", "created_at", "updated_at"]

admin.site.register(Product, ProductAdmin);
