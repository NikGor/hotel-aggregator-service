from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from hotel_service.hotels.models import Hotel
from hotel_service.metahotels.models import MetaHotel


class MetaHotelAndHotelTests(APITestCase):
    def setUp(self):
        # Создание тестовых данных для Hotel
        meta_hotel1 = MetaHotel.objects.create(id="mercure_pattaya")
        meta_hotel2 = MetaHotel.objects.create(id="windways")
        Hotel.objects.create(name="Mercure Pattaya", supplier_id="AAA", meta_hotel=meta_hotel1)
        Hotel.objects.create(name="Mercure Pattaya", supplier_id="BBB", meta_hotel=meta_hotel1)
        Hotel.objects.create(name="Windways Hotel", supplier_id="AAA", meta_hotel=meta_hotel2)

    def test_get_hotels(self):
        # Тест на получение списка отелей
        url = reverse('hotel-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
