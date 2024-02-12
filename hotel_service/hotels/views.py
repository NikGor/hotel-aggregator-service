from rest_framework import generics
from .models import Hotel, HotelBindingHistory
from .serializers import HotelSerializer, HotelBindingHistorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import views, status
from django.shortcuts import get_object_or_404
from ..metahotels.models import MetaHotel


class HotelList(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class HotelDetail(APIView):
    def get(self, request, hotel_id):
        try:
            hotel = Hotel.objects.get(pk=hotel_id)
            serializer = HotelSerializer(hotel)
            return Response(serializer.data)
        except Hotel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class HotelCreate(generics.CreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def perform_create(self, serializer):
        hotel = serializer.save()
        HotelBindingHistory.objects.create(hotel=hotel, meta_hotel=hotel.meta_hotel)


class ReassignHotelView(views.APIView):
    def post(self, request, *args, **kwargs):
        hotel_id = request.data.get('hotel_id')
        new_meta_hotel_id = request.data.get('new_meta_hotel_id')

        if not hotel_id or not new_meta_hotel_id:
            return Response({"error": "Необходимо указать 'hotel_id' и 'new_meta_hotel_id'."},
                            status=status.HTTP_400_BAD_REQUEST)

        hotel = get_object_or_404(Hotel, id=hotel_id)
        new_meta_hotel = get_object_or_404(MetaHotel, id=new_meta_hotel_id)

        hotel.meta_hotel = new_meta_hotel
        hotel.save()

        HotelBindingHistory.objects.create(hotel=hotel, meta_hotel=new_meta_hotel)

        return Response({"message": "Отель успешно перепривязан к новому мета-отелю."},
                        status=status.HTTP_200_OK)


class HotelBindingHistoryView(generics.ListAPIView):
    serializer_class = HotelBindingHistorySerializer

    def get_queryset(self):
        hotel_id = self.kwargs.get('hotel_id')
        return HotelBindingHistory.objects.filter(hotel__id=hotel_id).order_by('-timestamp')
