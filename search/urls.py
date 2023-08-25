from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('/tourist', views.tourist, name='tourist'),
    path('/tourist_price_sort', views.tourist_price_sort, name='tourist_price_sort'),
    path('/tourist_price_sort2', views.tourist_price_sort2, name='tourist_price_sort2'),
    path('/tourist_by', views.tourist_district, name='tourist_district'),
    path('/tourist_price_max', views.tourist_price_max, name='tourist_price_max'),
    path('/tourist_price_min', views.tourist_price_min, name='tourist_price_min'),

    path('/restaurant', views.restaurant, name='restaurant'),
    path('/restaurant_price_sort', views.restaurant_price_sort, name='restaurant_price_sort'),
    path('/restaurant_price_sort2', views.restaurant_price_sort2, name='restaurant_price_sort2'),
    path('/restaurant_by', views.restaurant_district, name='restaurant_district'),
    path('/restaurant_star_max', views.restaurant_star_max, name='restaurant_star_max'),
    path('/restaurant_price_min', views.restaurant_price_min, name='restaurant_price_min'),

    path('/hotel', views.hotel, name='hotel'),
    path('/hotel_price_sort', views.hotel_price_sort, name='hotel_price_sort'),
    path('/hotel_by', views.hotel_district, name='hotel_district'),
    path('/hotel_house_max', views.hotel_house_max, name='hotel_house_max'),
    path('/hotel_family_max', views.hotel_family_max, name='hotel_family_max'),
]
