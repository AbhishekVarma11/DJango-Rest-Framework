from rest_framework import viewsets,mixins

from .models import product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset=product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'
    
class ProductGenericViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    
    queryset=product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'
    
    
product_list_view2=ProductGenericViewSet.as_view({'get','list'})
product_detail_view2=ProductGenericViewSet.as_view({'get','retrieve'})   