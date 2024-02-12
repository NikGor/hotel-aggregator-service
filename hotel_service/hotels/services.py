from django.shortcuts import get_object_or_404
from .models import Hotel, HotelBindingHistory, MetaHotel
from django.db import transaction
from django.core.exceptions import ValidationError


# Create a binding history record when a hotel is assigned to a meta hotel.
def create_hotel_binding_history(hotel, meta_hotel):
    HotelBindingHistory.objects.create(hotel=hotel, meta_hotel=meta_hotel)


# Reassign a single hotel to a new meta hotel and create a binding history record.
def reassign_hotel(hotel_id, new_meta_hotel_id):
    with transaction.atomic():
        hotel = get_object_or_404(Hotel, id=hotel_id)
        new_meta_hotel = get_object_or_404(MetaHotel, id=new_meta_hotel_id)
        hotel.meta_hotel = new_meta_hotel
        hotel.save()
        create_hotel_binding_history(hotel, new_meta_hotel)
        return hotel


# Reassign multiple hotels to a new meta hotel and create binding history records.
def reassign_hotels(hotel_ids, new_meta_hotel_id):
    with transaction.atomic():
        for hotel_id in hotel_ids:
            try:
                reassign_hotel(hotel_id, new_meta_hotel_id)
            except ValidationError as e:
                raise e
                continue
