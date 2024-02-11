from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from hotel_service.metahotels.models import MetaHotel


class MetaHotelAndHotelTests(APITestCase):
    def setUp(self):
        # Создание тестовых данных для MetaHotel
        MetaHotel.objects.create(id="mercure_pattaya")
        MetaHotel.objects.create(id="windways")

    def test_get_meta_hotels(self):
        # Тест на получение списка мета-отелей
        url = reverse('meta-hotel-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
