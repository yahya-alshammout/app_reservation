# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_city = models.CharField(max_length=100)
    total_rooms = models.IntegerField()
    empty_rooms = models.IntegerField()
    def __str__(self):
        return self.hotel_name

class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=20)


    def __str__(self):
        return self.customer_name

class Reservation(models.Model):
    hotel = models.ForeignKey(Hotel)
    name = models.ForeignKey(Customer)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.hotel.hotel_name + " for " + self.name.customer_name

