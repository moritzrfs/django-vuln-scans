from django.urls import path

from . import views

namespace = "cars"
urlpatterns = [
    path('cars/', views.ListCars.as_view()),
    path('cars/create/', views.CreateCar.as_view()),
    path('cars/<int:car_id>/', views.CarDetail.as_view()),
]