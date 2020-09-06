from model_bakery import baker
from rest_framework import status
from rest_framework.test import APITestCase

from django.urls import reverse

class GetBrandsTest(APITestCase):
    """ Test module for GET brands """

    def setUp(self):
        self.brands = []
        self.brands.append(baker.make('cars.Brand', name='a'))
        self.brands.append(baker.make('cars.Brand', name='b'))
        self.brands_counter = len(self.brands)
        self.url = reverse('brands')

    def test_get_brands_valid(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), self.brands_counter)
        self.assertEqual(response.data['results'][0]['id'], self.brands[0].id)
        self.assertEqual(response.data['results'][1]['id'], self.brands[1].id)

