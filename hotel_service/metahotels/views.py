# from django.shortcuts import get_object_or_404
from rest_framework import generics  # , views
from .models import MetaHotel
from .serializers import MetaHotelSerializer
from rest_framework.response import Response
from rest_framework import status


class MetaHotelList(generics.ListAPIView):
    queryset = MetaHotel.objects.all()
    serializer_class = MetaHotelSerializer


class MetaHotelDetail(generics.RetrieveAPIView):
    def get(self, request, meta_hotel_id):
        try:
            metahotel = MetaHotel.objects.get(pk=meta_hotel_id)
            serializer = MetaHotelSerializer(metahotel)
            return Response(serializer.data)
        except MetaHotel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


# class CombineHotelsView(views.APIView):
#     def post(self, request, *args, **kwargs):
#         hotel_ids = request.data.get('hotel_ids')
#         meta_hotel_id = request.data.get('meta_hotel_id')
#
#         if not hotel_ids or not meta_hotel_id:
#             return Response({"error": "Необходимо указать 'meta_hotel_id' и 'hotel_ids'."},
#                             status=status.HTTP_400_BAD_REQUEST)
#
#         meta_hotel = get_object_or_404(MetaHotel, id=meta_hotel_id)
#
#         hotels = Hotel.objects.filter(id__in=hotel_ids)
#         for hotel in hotels:
#             hotel.meta_hotel = meta_hotel
#             hotel.save()
#
#         serializer = HotelSerializer(hotels, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
