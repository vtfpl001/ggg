from django.contrib import admin
from .models import Product
from .models import Certificate

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'packing', 'weight', 'rate', 'grade']
    list_filter = ['grade']
    search_fields = ['name', 'grade']


# In vtapp/admin.py

from django.contrib import admin



@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('certificate_name', 'description',)  # Add more fields if needed


