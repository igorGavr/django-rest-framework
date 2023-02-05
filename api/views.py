from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from django.forms.models import model_to_dict
from products.serializers import ProductSerializer


@api_view(['GET'])
def api_home(request, *args, **kwargs):

    instance = Product.objects.all().order_by("?").first()
    date = {}
    if instance:
        data = ProductSerializer(instance).data
    return Response(data)



