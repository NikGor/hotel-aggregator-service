from django.urls import path
from hotel_service.metahotels.views import MetaHotelList, MetaHotelDetail

urlpatterns = [
    path('', MetaHotelList.as_view(), name='meta-hotel-list'),
    path('<str:meta_hotel_id>/', MetaHotelDetail.as_view(), name='meta-hotel-detail'),
]
