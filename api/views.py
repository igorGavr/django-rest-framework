from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.

def api_home(request, *args, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.load(body)
    except:
        pass
    print(data)
    print(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)
