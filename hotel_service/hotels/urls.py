from django.urls import path
from hotel_service.hotels.views import (HotelList,
                                        HotelDetail,
                                        HotelCreate,
                                        ReassignHotelView,
                                        HotelBindingHistoryView,
                                        CombineHotelsView)

urlpatterns = [
    path('', HotelList.as_view(), name='hotel-list'),
    path('<int:hotel_id>/', HotelDetail.as_view(), name='hotel-detail'),
    path('create/', HotelCreate.as_view(), name='hotel-create'),
    path('reassign-hotel/', ReassignHotelView.as_view(), name='reassign-hotel'),
    path('combine-hotels/', CombineHotelsView.as_view(), name='combine-hotels'),
    path('<int:hotel_id>/binding-history/',
         HotelBindingHistoryView.as_view(),
         name='hotel-binding-history'),
]
