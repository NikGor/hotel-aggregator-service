from rest_framework import generics
from .models import MetaHotel
from .serializers import MetaHotelSerializer


# Lists all MetaHotel instances using DRF's generic ListAPIView.
class MetaHotelList(generics.ListAPIView):
    queryset = MetaHotel.objects.all()
    serializer_class = MetaHotelSerializer


# Retrieves a single MetaHotel instance using DRF's generic RetrieveAPIView.
class MetaHotelDetail(generics.RetrieveAPIView):
    queryset = MetaHotel.objects.all()
    serializer_class = MetaHotelSerializer
    lookup_url_kwarg = 'meta_hotel_id'
