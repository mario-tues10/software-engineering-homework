from django.urls import include, path
from elsys import views

urlpatterns = [
    path('', views.index),
    path('home', views.home), // the name is not descriptive
    path('about', views.about), 
    path('cars', views.cars), 
]
