from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r"allhotels", AllHotels),
    url(r"hotelincity", HotelInCity),
    url(r"reservationlist", ReservationList),
]
