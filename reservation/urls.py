from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r"allhotels", AllHotels),
    url(r"allcustomers", AllCustomers),
    url(r"allreservations", AllReservations),
]
