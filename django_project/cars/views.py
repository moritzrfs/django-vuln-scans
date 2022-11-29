from django.shortcuts import render
from rest_framework.response import Response
# import views from rest framework
from rest_framework import viewsets

# import CarSerializer from serializers.py
from .serializers import CarSerializer, CreateCarSerializer
from rest_framework.views import APIView

# import Car from models.py
from .models import Car

# Create your views here.

class ListCars(APIView):
    def get(self, request):
        cars = Car.objects.all()
        data = CarSerializer(cars, many=True).data
        return Response(data)

class CreateCar(APIView):
    def post(self, request):
        car = CreateCarSerializer(data=request.data)
        if car.is_valid():
            car.save()
            return Response(car.data, status=201)
        else:
            return Response(car.errors, status=400)