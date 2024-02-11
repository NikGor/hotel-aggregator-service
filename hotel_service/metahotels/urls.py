from django.urls import path
from hotel_service.metahotels.views import MetaHotelList

urlpatterns = [
    path('meta-hotels/', MetaHotelList.as_view(), name='meta-hotel-list'),
]
