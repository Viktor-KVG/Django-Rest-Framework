from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from testy.models import *
from alco.urls import *

class TestyTests(APITestCase):
    def test_level(self):
        response = self.client.get(Level.name_obj)
        print(response.data)
        # url = reverse('account-list')
        # data = {'name': 'DabApps'}
        # response = self.client.post(url, data, format='json')
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(Account.objects.count(), 1)
        # self.assertEqual(Account.objects.get().name, 'DabApps')
