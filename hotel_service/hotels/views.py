from rest_framework import generics
from .models import Hotel
from .serializers import HotelSerializer


class HotelList(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
