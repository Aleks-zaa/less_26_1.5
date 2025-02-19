from rest_framework import status
from rest_framework.test import APITestCase

from vehicle.models import Car


class VehicleTestCase(APITestCase):

    def setUp(self):
        pass

    def test_create_car(self):
        """Тестирование создания машины"""
        data = {
            "title": "Test",
            "description": "Test"
        }
        response = self.client.post("/cars/", data=data)
        print(response.json())

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(),
                         {'id': 1, 'milage': [], 'title': 'Test', 'description': 'Test', 'owner': None})
        self.assertTrue(Car.objects.all().exists())

    def test_list_car(self):
        """Тестирования вывода списка машин"""
        Car.objects.create(
                title="list_test",
                description="list_test"
                   )

        response = self.client.get('/cars/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json(),
                         [{'id': 2, 'milage': [], 'title': 'list_test', 'description': 'list_test', 'owner': None}])
