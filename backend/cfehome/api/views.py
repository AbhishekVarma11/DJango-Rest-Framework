from django.shortcuts import render
from django.http import JsonResponse
import json
def api_home(request,*args,**kwargs):
    body=request.body 
    data={}
    try:
        data=json.loads(body)
    except:
        pass
    print(data)
    data['headers']=dict(request.headers)
    data['content_type']=request.content_type
    print(request.GET)
    return JsonResponse(data)
