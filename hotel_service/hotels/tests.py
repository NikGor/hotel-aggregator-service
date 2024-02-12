from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from hotel_service.hotels.models import Hotel, HotelBindingHistory
from hotel_service.metahotels.models import MetaHotel


class HotelTests(APITestCase):
    def setUp(self):
        self.meta_hotel1 = MetaHotel.objects.create(id="mercure_pattaya")
        self.meta_hotel2 = MetaHotel.objects.create(id="windways")

        Hotel.objects.create(name="Mercure Pattaya", supplier_id="AAA", meta_hotel=self.meta_hotel1)
        Hotel.objects.create(name="Mercure Pattaya", supplier_id="BBB", meta_hotel=self.meta_hotel1)

        self.hotel = Hotel.objects.create(name="Windways Hotel", supplier_id="AAA", meta_hotel=self.meta_hotel1)

    def test_get_hotels(self):
        url = reverse('hotel-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_get_hotel_detail(self):
        url = reverse('hotel-detail', args=[self.hotel.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.hotel.name)

    def test_create_hotel(self):
        url = reverse('hotel-create')

        data = {
            'name': 'New Hotel',
            'supplier_id': 'CCC',
            'meta_hotel': 'mercure_pattaya'
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        hotel = Hotel.objects.get(name='New Hotel')
        self.assertIsNotNone(hotel)
        self.assertEqual(hotel.supplier_id, 'CCC')
        self.assertEqual(hotel.meta_hotel.id, 'mercure_pattaya')

    def test_reassign_hotel(self):
        url = reverse('reassign-hotel')
        data = {
            'hotel_id': self.hotel.id,
            'new_meta_hotel_id': self.meta_hotel2.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.hotel.refresh_from_db()
        self.assertEqual(self.hotel.meta_hotel.id, self.meta_hotel2.id)


class HotelBindingHistoryTests(APITestCase):
    def test_get_binding_history(self):
        meta_hotel = MetaHotel.objects.create(id="mercure_pattaya")
        hotel = Hotel.objects.create(name="Windways Hotel", supplier_id="AAA", meta_hotel=meta_hotel)
        HotelBindingHistory.objects.create(hotel=hotel, meta_hotel=meta_hotel)

        url = reverse('hotel-binding-history', kwargs={'hotel_id': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
