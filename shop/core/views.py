from django.shortcuts import render
from rest_framework import viewsets

from core.models import Customer, Product, Transaction
from core.serializers import CustomerSerializer, ProductSerializer, TransactionSerializer


class CustomerView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class TransactionView(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
