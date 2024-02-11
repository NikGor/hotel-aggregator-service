from rest_framework import generics
from .models import MetaHotel
from .serializers import MetaHotelSerializer


class MetaHotelList(generics.ListAPIView):
    queryset = MetaHotel.objects.all()
    serializer_class = MetaHotelSerializer
