from django.urls import path
from hotel_service.hotels.views import HotelList

urlpatterns = [
    path('hotels/', HotelList.as_view(), name='hotel-list'),
]
