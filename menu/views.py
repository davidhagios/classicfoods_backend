from django.shortcuts import render
from rest_framework import viewsets
from .models import FoodItem
from .serializers import FoodItemSerializer

# Create your views here.
class FoodItemViewSet(viewsets.ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
