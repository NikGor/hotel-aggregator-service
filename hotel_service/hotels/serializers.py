from rest_framework import serializers
from hotel_service.hotels.models import Hotel, HotelBindingHistory


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class HotelBindingHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelBindingHistory
        fields = ['meta_hotel', 'timestamp']


class ReassignHotelSerializer(serializers.Serializer):
    hotel_id = serializers.IntegerField()
    new_meta_hotel_id = serializers.IntegerField()


class CombineHotelsSerializer(serializers.Serializer):
    hotel_ids = serializers.ListField(child=serializers.IntegerField())
    new_meta_hotel_id = serializers.IntegerField()
