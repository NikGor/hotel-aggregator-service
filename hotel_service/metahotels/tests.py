from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from hotel_service.hotels.models import Hotel
from hotel_service.metahotels.models import MetaHotel


class MetaHotelAndHotelTests(APITestCase):
    def setUp(self):
        MetaHotel.objects.create(id="mercure_pattaya")
        MetaHotel.objects.create(id="windways")

        Hotel.objects.create(name="Hotel 1", supplier_id="AAA", meta_hotel=MetaHotel.objects.get(id="mercure_pattaya"))
        Hotel.objects.create(name="Hotel 2", supplier_id="AAA", meta_hotel=MetaHotel.objects.get(id="mercure_pattaya"))
        Hotel.objects.create(name="Hotel 3", supplier_id="BBB", meta_hotel=MetaHotel.objects.get(id="windways"))

    def test_get_meta_hotels(self):
        url = reverse('meta-hotel-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        for meta_hotel_data in response.data:
            self.assertTrue('hotels' in meta_hotel_data)
            self.assertIsInstance(meta_hotel_data['hotels'], list)

            self.assertTrue(len(meta_hotel_data['hotels']) > 0)

    def test_get_meta_hotel_detail(self):
        url = reverse('meta-hotel-detail', args=["mercure_pattaya"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], "mercure_pattaya")
