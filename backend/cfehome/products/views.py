from django.shortcuts import render

from rest_framework import generics 

from .models import product
from .serializers import ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset=product.objects.all()
    serializer_class=ProductSerializer
    #lookup_field='pk'
    
product_detail_view=ProductDetailAPIView.as_view()
