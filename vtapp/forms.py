from django import forms
from .models import Product, Certificate

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = '__all__'
