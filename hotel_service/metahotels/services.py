from django.shortcuts import get_object_or_404
from .models import MetaHotel


# Retrieves a MetaHotel instance by its ID or raises Http404.
def get_metahotel_by_id(meta_hotel_id):
    return get_object_or_404(MetaHotel, pk=meta_hotel_id)
