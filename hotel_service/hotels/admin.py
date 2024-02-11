from django.contrib import admin
from .models import Hotel


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'supplier_id', 'meta_hotel')
    list_filter = ('meta_hotel',)
    search_fields = ('name', 'supplier_id', 'meta_hotel__id')
    raw_id_fields = ('meta_hotel',)
