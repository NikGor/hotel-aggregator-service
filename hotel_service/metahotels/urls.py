from django.urls import path
from hotel_service.metahotels.views import MetaHotelList, MetaHotelDetail  # , CombineHotelsView

urlpatterns = [
    path('', MetaHotelList.as_view(), name='meta-hotel-list'),
    path('<str:meta_hotel_id>/', MetaHotelDetail.as_view(), name='meta-hotel-detail'),
    # path('combine-hotels/', CombineHotelsView.as_view(), name='combine-hotels'),
]
