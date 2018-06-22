# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import *
def AllHotels(request):
    all_hotels = "<ul>"
    for hotel in Hotel.objects.all():
        all_hotels += "<li>" + hotel.hotel_name + "</li>"
    all_hotels += "</ul>"
    return HttpResponse(all_hotels)
def HotelInCity(request1):
    all_hotels  = "<ul>"
    for hotel in Hotel.objects.all():
        if hotel.hotel_city in all_hotels:
            continue
        all_hotels += "<h2>" + hotel.hotel_city + "</h2>"
    for hotel1 in Hotel.objects.all():
        all_hotels += "<ul> <h5>" + hotel1.hotel_name + "</h5> </ul>"
    all_hotels += "</ul>"
    return  HttpResponse(all_hotels)
def ReservationList(request):
    all_reservation = "<ul>"
    for reserve in Reservation.objects.all():
        all_reservation += "<h3>" + reserve.hotel.hotel_name + " <> " + reserve.name.customer_name + "</h3>"
        all_reservation += "<ul> <h5>" + " enter hotel : " + str(reserve.start_time) + "</h5> </ul>"
        all_reservation += "<ul> <h5>" + " exit hotel : " + str(reserve.end_time) + "</h5> </ul>"
        all_reservation += "<ul>"
        return HttpResponse(all_reservation)







