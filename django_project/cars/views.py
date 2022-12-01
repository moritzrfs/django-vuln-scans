from django.shortcuts import render
from rest_framework.response import Response
# import views from rest framework
from rest_framework import viewsets

# import CarSerializer from serializers.py
from .serializers import CarSerializer, CreateCarSerializer
from rest_framework.views import APIView

# import Car from models.py
from .models import Car
from drf_roles.mixins import RoleViewSetMixin

class ListCars(APIView, RoleViewSetMixin):
    permission_classes = []
    def get(self, request):
        # only return electric cars
        cars = Car.objects.filter(engine='EV')
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)



class CreateCar(APIView):
    def post(self, request):
        car = CreateCarSerializer(data=request.data)
        if car.is_valid():
            car.save()
            return Response(car.data, status=201)
        else:
            return Response(car.errors, status=400)

class CarDetail(APIView):
    permission_classes = []
    def get(self, request, car_id):
        car = Car.objects.get(id=car_id)
        serializer = CarSerializer(car)
        return Response(serializer.data)

    def post(self, request, car_id):
        car = Car.objects.get(id=car_id)
        updated_car = CarSerializer(car, data=request.data)
        if updated_car.is_valid():
            updated_car.save()
            return Response(updated_car.data)
        else:
            return Response(updated_car.errors, status=400)
