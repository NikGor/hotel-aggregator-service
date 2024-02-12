from rest_framework import serializers
from hotel_service.hotels.serializers import HotelSerializer
from hotel_service.metahotels.models import MetaHotel


class MetaHotelSerializer(serializers.ModelSerializer):
    hotels = HotelSerializer(many=True, read_only=True)

    class Meta:
        model = MetaHotel
        fields = ['id', 'hotels']
