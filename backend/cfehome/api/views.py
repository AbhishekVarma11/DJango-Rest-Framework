from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json
from products.models import product
# def api_home(request,*args,**kwargs):
    
#     model_data=product.objects.all().order_by("?").first()
#     data={}
#     if model_data:
#         data=model_to_dict(model_data,fields=['id','title'])
#         # data['id']=model_data.id
#         # data['title']=model_data.title
#         # data['content']=model_data.content 
#         # data['price']=model_data.price 
            
#     return JsonResponse(data)

from rest_framework.decorators import api_view

from rest_framework.response import Response
from products.serializers import ProductSerializer
@api_view(["GET"])
def api_home(request,*args,**kwargs):
    instance=product.objects.all().order_by("?").first()
    data={}
    if instance:
        #data=model_to_dict(model_data,fields=['id','title','price'])
        data=ProductSerializer(instance).data
    return Response(data)


