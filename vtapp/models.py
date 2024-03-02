from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    packing = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    rate = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)  # Allow rate to be null and empty
    specification = models.TextField(null=True, blank=True)  # Allow specification to be null and empty
    grade = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='product_photos/')

class Certificate(models.Model):
    certificate_name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)  # Allow description to be null and empty
    photo = models.ImageField(upload_to='certificates/')
