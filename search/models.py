from django.db import models


# Create your models here.
class TourPlace(models.Model):
    tour_id = models.AutoField
    tour_state = models.CharField(max_length=50)
    tour_city = models.CharField(max_length=50)
    tour_district = models.CharField(max_length=50)
    tour_price = models.DecimalField(max_digits=10, decimal_places=5)
    tour_open_time = models.TimeField()
    tour_close_time = models.TimeField()
    tour_area = models.DecimalField(max_digits=10, decimal_places=5)
    tour_capacity = models.IntegerField()
    tour_build_date = models.DateField(max_length=50)


class Restaurant(models.Model):
    rst_id = models.AutoField
    rst_state = models.CharField(max_length=50)
    rst_city = models.CharField(max_length=50)
    rst_district = models.CharField(max_length=50)
    rst_price = models.DecimalField(max_digits=10, decimal_places=5)
    rst_open_time = models.TimeField()
    rst_close_time = models.TimeField()
    rst_cookies_n = models.IntegerField()
    rst_star = models.CharField(max_length=50)  # 5/4/3 star
    rst_type = models.CharField(max_length=50)


class Hotel(models.Model):
    hotel_id = models.AutoField
    hotel_state = models.CharField(max_length=50)
    hotel_city = models.CharField(max_length=50)
    hotel_district = models.CharField(max_length=50)
    hotel_price = models.DecimalField(max_digits=10, decimal_places=5)
    hotel_star = models.CharField(max_length=50)  # 5/4/3 star
    hotel_house_n = models.IntegerField()
    hotel_single_n = models.IntegerField()
    hotel_double_n = models.IntegerField()
    hotel_family_n = models.IntegerField()

