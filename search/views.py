from django.shortcuts import render
from django.db.models import Max, Min
from .models import *


# Create your views here.

def index(request):
    return render(request, 'search/base.html')


def tourist(request):
    tour_list = TourPlace.objects.all()
    c = {"tour_list": tour_list}
    return render(request, 'search/tourist.html', c)


def tourist_price_sort(request):
    tour_list_sort = TourPlace.objects.order_by('tour_price')
    c = {"tour_list": tour_list_sort}
    return render(request, 'search/tourist.html', c)


def tourist_price_sort2(request):
    tour_list_sort = TourPlace.objects.order_by('tour_price')
    c = {"tour_list": tour_list_sort[::-1]}
    return render(request, 'search/tourist.html', c)


def tourist_district(request):
    sel_district = request.GET['district']
    if sel_district != '':
        tour_list = TourPlace.objects.filter(tour_district=sel_district)
        c = {"tour_list": tour_list, "sel_district": sel_district}
    else:
        tour_list = TourPlace.objects.all()
        c = {"tour_list": tour_list, "sel_district": sel_district}
    return render(request, 'search/tourist.html', c)


def tourist_price_max(request):
    md = TourPlace.objects.all().aggregate(Max('tour_price'))
    mdv = md['tour_price__max']
    tour_list = TourPlace.objects.filter(tour_price=mdv)
    c = {"tour_list": tour_list}
    return render(request, 'search/tourist.html', c)


def tourist_price_min(request):
    md = TourPlace.objects.all().aggregate(Min('tour_price'))
    mdv = md['tour_price__min']
    tour_list = TourPlace.objects.filter(tour_price=mdv)
    c = {"tour_list": tour_list}
    return render(request, 'search/tourist.html', c)


def restaurant(request):
    rest_list = Restaurant.objects.all()
    c = {"rest_list": rest_list}
    return render(request, 'search/rest.html', c)


def restaurant_price_sort(request):
    rest_list_sort = Restaurant.objects.order_by('rst_price')
    c = {"rest_list": rest_list_sort}
    return render(request, 'search/rest.html', c)


def restaurant_price_sort2(request):
    rest_list_sort = Restaurant.objects.order_by('rst_price')
    c = {"rest_list": rest_list_sort[::-1]}
    return render(request, 'search/rest.html', c)


def restaurant_district(request):
    sel_district = request.GET['district']
    if sel_district != '':
        rest_list = Restaurant.objects.filter(rst_district=sel_district)
        c = {"rest_list": rest_list, "sel_district": sel_district}
    else:
        rest_list = Restaurant.objects.all()
        c = {"rest_list": rest_list, "sel_district": sel_district}
    return render(request, 'search/rest.html', c)


def restaurant_star_max(request):
    md = Restaurant.objects.all().aggregate(Max('rst_star'))
    mdv = md['rst_star__max']
    rest_list = Restaurant.objects.filter(rst_star=mdv)
    c = {"rest_list": rest_list}
    return render(request, 'search/rest.html', c)


def restaurant_price_min(request):
    md = Restaurant.objects.all().aggregate(Min('rst_price'))
    mdv = md['rst_price__min']
    rest_list = Restaurant.objects.filter(rst_price=mdv)
    c = {"rest_list": rest_list}
    return render(request, 'search/rest.html', c)


def hotel(request):
    hotel_list = Hotel.objects.all()
    c = {"hotel_list": hotel_list}
    return render(request, 'search/hotel.html', c)


def hotel_price_sort(request):
    hotel_list_sort = Hotel.objects.order_by('hotel_price')
    c = {"hotel_list": hotel_list_sort}
    return render(request, 'search/hotel.html', c)


def hotel_district(request):
    sel_district = request.GET['district']
    if sel_district != '':
        hotel_list = Hotel.objects.filter(hotel_district=sel_district)
        c = {"hotel_list": hotel_list, "sel_district": sel_district}
    else:
        hotel_list = Hotel.objects.all()
        c = {"hotel_list": hotel_list, "sel_district": sel_district}
    return render(request, 'search/hotel.html', c)


def hotel_house_max(request):
    md = Hotel.objects.all().aggregate(Max('hotel_house_n'))
    mdv = md['hotel_house_n__max']
    hotel_list = Hotel.objects.filter(hotel_house_n=mdv)
    c = {"hotel_list": hotel_list}
    return render(request, 'search/hotel.html', c)


def hotel_family_max(request):
    md = Hotel.objects.all().aggregate(Max('hotel_family_n'))
    mdv = md['hotel_family_n__max']
    hotel_list = Hotel.objects.filter(hotel_family_n=mdv)
    c = {"hotel_list": hotel_list}
    return render(request, 'search/hotel.html', c)
