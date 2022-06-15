from os import name
from django.urls import path
from . import views

urlpatterns = [

    path('',views.loading,name="loading"),
    path('homePage/',views.homePage,name="homePage"),
    path('homePage/bmiResult',views.bmiResult,name="homePage"),
    path('homePage/HeartDiseasePredictionResult',views.HeartDiseasePredictionResult,name="homePage")

 
]
