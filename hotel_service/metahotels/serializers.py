from rest_framework import serializers
from hotel_service.hotels.models import MetaHotel


class MetaHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaHotel
        fields = '__all__'
