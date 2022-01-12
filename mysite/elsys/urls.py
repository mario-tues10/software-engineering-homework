from django.urls import include, path
from elsys import views

urlpatterns = [
    path('', views.index),
    path('home', views.home),
    path('about', views.about),
    path('cars', views.cars),
    path('longest_comment', views.longest_comment),
    path('post_with_longest_title', views.post_with_longest_title),
    path('get_data', views.get_data),
    path('get_min', views.get_min),
    path('get_max', views.get_max),
    path('get_avg', views.get_avg)
]
