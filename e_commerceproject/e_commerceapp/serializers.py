from rest_framework import serializers
from .models import Category, Product, Customer


class customerserializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'First_name','Last_name', 'phonenumber', 'email', 'address','date_created']
        model = Customer


class categoryserializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'title']
        model = Category


class productserializer(serializers.ModelSerializer):
    class Meta:
        fields = ['product_name', 'category', 'price', 'quantity', 'description', 'img', 'status', 'date_created']
        model = Product
