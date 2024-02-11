from django.contrib import admin
from .models import MetaHotel


@admin.register(MetaHotel)
class MetaHotelAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('id',)
