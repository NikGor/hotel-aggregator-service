from django.shortcuts import get_object_or_404
from rest_framework import generics, status, views
from rest_framework.response import Response
from .models import Hotel, HotelBindingHistory
from .serializers import HotelSerializer, HotelBindingHistorySerializer, ReassignHotelSerializer, \
    CombineHotelsSerializer
from .services import create_hotel_binding_history, reassign_hotel, reassign_hotels
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema


# Lists all hotels using a generic list view provided by DRF.
class HotelList(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


# Retrieves detail for a single hotel. Uses APIView for a more customized handling.
class HotelDetail(views.APIView):
    def get(self, request, hotel_id):
        hotel = get_object_or_404(Hotel, pk=hotel_id)
        serializer = HotelSerializer(hotel)
        return Response(serializer.data)


# Lists the binding history for a specific hotel.
class HotelBindingHistoryView(generics.ListAPIView):
    serializer_class = HotelBindingHistorySerializer

    def get_queryset(self):
        hotel_id = self.kwargs.get('hotel_id')
        return HotelBindingHistory.objects.filter(hotel__id=hotel_id).order_by('-timestamp')


# Handles creation of new hotels and logs the initial meta hotel assignment in the binding history.
class HotelCreate(generics.CreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def perform_create(self, serializer):
        hotel = serializer.save()
        create_hotel_binding_history(hotel, hotel.meta_hotel)


# Reassigns a single hotel to a new meta hotel.
class ReassignHotelView(APIView):
    serializer_class = ReassignHotelSerializer

    @swagger_auto_schema(request_body=ReassignHotelSerializer)
    def post(self, request, *args, **kwargs):
        hotel_id = request.data.get('hotel_id')
        new_meta_hotel_id = request.data.get('new_meta_hotel_id')

        if not hotel_id or not new_meta_hotel_id:
            return Response({"error": "You must specify 'hotel_id' and 'new_meta_hotel_id'."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            hotel = reassign_hotel(hotel_id, new_meta_hotel_id)
            success_message = (f"The hotel {hotel.name} has been successfully "
                               f"reassigned to the new meta-hotel {hotel.meta_hotel.id}.")
            return Response({"message": success_message}, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# Combines multiple hotels into a single meta hotel.
class CombineHotelsView(APIView):
    serializer_class = CombineHotelsSerializer

    @swagger_auto_schema(request_body=CombineHotelsSerializer)
    def post(self, request, *args, **kwargs):
        hotel_ids = request.data.get('hotel_ids')
        new_meta_hotel_id = request.data.get('new_meta_hotel_id')

        if not hotel_ids or not new_meta_hotel_id:
            return Response({"error": "You must specify 'hotel_ids' and 'new_meta_hotel_id'."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            reassign_hotels(hotel_ids, new_meta_hotel_id)
            return Response({"message": "The hotels have been successfully reassigned to the new meta-hotel."},
                            status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
