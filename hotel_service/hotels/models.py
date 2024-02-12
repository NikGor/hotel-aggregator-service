from django.db import models
from hotel_service.metahotels.models import MetaHotel
from django.utils import timezone


class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    supplier_id = models.CharField(max_length=255)
    meta_hotel = models.ForeignKey(MetaHotel, on_delete=models.SET_NULL, null=True, related_name='hotels')

    def __str__(self):
        return f"{self.name} ({self.supplier_id})"


class HotelBindingHistory(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='binding_history')
    meta_hotel = models.ForeignKey(MetaHotel, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.hotel.name} -> {self.meta_hotel.id} at {self.timestamp}"
