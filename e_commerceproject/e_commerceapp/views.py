from django.shortcuts import render
from rest_framework import generics
from .models import Category, Product, Customer
from .serializers import categoryserializer, productserializer, customerserializer


# Create your views here.
class ListCustomer(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = customerserializer


class DetailCustomer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = customerserializer


class ListCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = categoryserializer


class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = categoryserializer


class ListProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = productserializer


class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = productserializer
