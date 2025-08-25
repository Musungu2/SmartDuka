from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Category, Product
from .serializers import ProductSerializer, CategorySerializer

# Create your views here.
