from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json

from products.models import Product
from django.forms.models import model_to_dict


def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=["id", "title"])
    print(data)
    return HttpResponse(data)



# def api_home(request, *args, **kwargs):
#     print(request.GET)
#     print(request.POST)
#     body = request.body
#     data = {"con":"hi"}
#     try:
#         data = json.load(body)
#     except:
#         pass
#
#     data["params"] = dict(request.GET)
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type
#     print(data)
#     return JsonResponse(data)
