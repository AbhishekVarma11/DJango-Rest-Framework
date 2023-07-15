from django.shortcuts import render

from rest_framework import generics 

from .models import product
from .serializers import ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset=product.objects.all()
    serializer_class=ProductSerializer
    #lookup_field='pk'
    
product_detail_view=ProductDetailAPIView.as_view()

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset=product.objects.all()
    serializer_class=ProductSerializer
    
    def perform_create(self,serializer):
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        if content is None:
            content=title
        serializer.save(content=content)
    
product_list_create_view=ProductListCreateAPIView.as_view()

# class ProductListAPIView(generics.ListAPIView):
#     queryset=product.objects.all()
#     serializer_class=ProductSerializer
#     #lookup_field='pk'
    
# product_list_view=ProductListAPIView.as_view()