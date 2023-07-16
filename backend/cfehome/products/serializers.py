from django import forms 
from .models import product
from rest_framework import serializers
class ProductSerializer(serializers.ModelSerializer):
    my_discount=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=product
        fields=[
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            "my_discount",
        ]
        
    def get_my_discount(self,obj):
        if not hasattr(obj,'id'):
            return None
        if not isinstance(obj,product):
            return None