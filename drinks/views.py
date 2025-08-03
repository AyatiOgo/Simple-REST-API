from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Drink
from .serializers import DrinkSerializer


# Create your views here.

@api_view(['GET', 'POST'])
def get_drinks(request):

    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many = True)
        return Response(serializer.data, status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = DrinkSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])    
def drink_info(request, pk):
    drink = Drink.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data, status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)

