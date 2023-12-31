from django.shortcuts import render,get_object_or_404

from rest_framework import generics,mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.authentication import TokenAuthentication
from api.mixins import StaffEditorPermissionMixin
from .models import product
from .serializers import ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset=product.objects.all()
    serializer_class=ProductSerializer
    #lookup_field='pk'
    
product_detail_view=ProductDetailAPIView.as_view()

class ProductListCreateAPIView(generics.ListCreateAPIView,StaffEditorPermissionMixin):
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

class ProductUpdateAPIView(generics.UpdateAPIView,StaffEditorPermissionMixin):
    queryset=product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'   
    def perform_update(self, serializer):
        instance=serializer.save()
        if not instance.content:
            instance.content=instance.title
    
product_update_view=ProductUpdateAPIView.as_view()

class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset=product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'
    
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
    
product_delete_view=ProductDestroyAPIView.as_view()

@api_view(["GET","POST"])
def product_alt_view(request,pk=None,*args,**kwargs):
    method=request.method 
    
    if method=="GET":
        #detail_view,list_view 
        if pk is not None:
            obj=get_object_or_404(product,pk=pk)
            data=ProductSerializer(obj,many=False).data
            return Response(data)
   
        qs=product.objects.all()
        data=ProductSerializer(qs,many=True).data
        return Response(data)
    if method=="POST":
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title=serializer.validated_data.get('title')
            content=serializer.validated_data.get('content') or None
            if content is None:
                content=title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid":"invalid data"},status=400)

class ProductMixinView(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset=product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'
                   
    def get(self,request,*args,**kwargs):
        pk=kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    def perform_create(self,serializer):
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        if content is None:
            content=title
        serializer.save(content=content)
    
product_mixin_view=ProductMixinView.as_view()
        

