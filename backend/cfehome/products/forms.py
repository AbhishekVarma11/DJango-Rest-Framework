from django import forms 
from .models import product

class ProductForm(forms.ModelForm):
    class Meta:
        model=product
        fields=[
            'title',
            'content',
            'price',
            'sale_price',
            
        ]