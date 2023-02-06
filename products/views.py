from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    ListAPIView, get_object_or_404, GenericAPIView,
    RetrieveUpdateDestroyAPIView, ListCreateAPIView
)
from rest_framework.mixins import (
    ListModelMixin, CreateModelMixin, RetrieveModelMixin,
    UpdateModelMixin, DestroyModelMixin
)


# //////////////////////////////
# ///        ListAPIView
# ///        ListCreateAPIView
# ///    RetrieveUpdateDestroyAPIView
# //////////////////////////////
# # ListAPIView = GenericAPIView + ListModelMixin
# # ListCreateAPIView = GenericAPIView + ListModelMixin + CreateModelMixin
# # RetrieveUpdateDestroyAPIView = GenericAPIView + RetrieveModelMixin + UpdateModelMixin + DestroyModelMixin
class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# //////////////////////////////
# ///   GenericAPIView + mixin
# //////////////////////////////
# class ProductListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#     def get(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)
#
#
# class ProductRetrieveUpdateDestroyView(
#     GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#     def get(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return super().partial_update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)


# /////////////////////////
# ///   GenericAPIView
# /////////////////////////
# class ProductListCreateView(GenericAPIView):
#     queryset = Product.objects.all()
#
#     def get(self, *args, **kwargs):
#         serializer = ProductSerializer(self.get_queryset(), many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         serializer = ProductSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_201_CREATED)
#
#
# class ProductRetrieveUpdateDestroyView(GenericAPIView):
#     queryset = Product.objects.all()
#
#     def get(self, *args, **kwargs):
#         product = self.get_object()
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#
#     def put(self, *args, **kwargs):
#         data = self.request.data
#         product = self.get_object()
#         serializer = ProductSerializer(product, data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         data = self.request.data
#         product = self.get_object()
#         serializer = ProductSerializer(product, data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         self.get_object().delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# /////////////////////////
# ///   APIView
# /////////////////////////
# class ProductListCreateView(APIView):
#     def get(self, *args, **kwargs):
#         products = Product.objects.all()
#         serializer = ProductSerializer(instance=products, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         serializer = ProductSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_201_CREATED)
#
#
# class ProductRetrieveUpdateDestroyView(APIView):
#     def get(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#         qs = Product.objects.all()
#         product = get_object_or_404(qs, pk=pk)
#         # exist = Product.objects.filter(pk=pk).exists()
#         # if not exist:
#         #     return Response('Not found', status.HTTP_404_NOT_FOUND)
#         # product = Product.objects.get(pk=pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#         qs = Product.objects.all()
#         data = self.request.data
#         product = get_object_or_404(qs, pk=pk)
#         # exist = Product.objects.filter(pk=pk).exists()
#         # if not exist:
#         #     return Response('Not found', status.HTTP_404_NOT_FOUND)
#         # product = Product.objects.get(pk=pk)
#         serializer = ProductSerializer(product, data)
#         # if not serializer.is_valid():
#         #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#         qs = Product.objects.all()
#         data = self.request.data
#         product = get_object_or_404(qs, pk=pk)
#         # exist = Product.objects.filter(pk=pk).exists()
#         # if not exist:
#         #     return Response('Not found', status.HTTP_404_NOT_FOUND)
#         # product = Product.objects.get(pk=pk)
#         serializer = ProductSerializer(product, data, partial=True)
#         # if not serializer.is_valid():
#         #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#         qs = Product.objects.all()
#         # exists = Product.objects.filter(pk=pk).exists()
#         # if not exists:
#         #     return Response('Not found', status.HTTP_404_NOT_FOUND)
#         # product = Product.objects.get(pk=pk)
#         product = get_object_or_404(qs, pk=pk)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
