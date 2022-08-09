from django.test import RequestFactory
from rest_framework.test import APIClient, APITestCase
from rest_framework import status



class DateTestCase(APITestCase):

    def test_get_date(self):
        factory = RequestFactory()
        url = 'http://127.0.0.1:8000/api/tohijri'
        date = {'year': 2022, 'month': 12, 'day': 12}
        request = factory.get(url, **date)
        print(request.headers, status.HTTP_200_OK)


class MonthsTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get_months(self):
        url = 'http://127.0.0.1:8000/api/months/hijri'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class WeekDaysTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get_days(self):
        url = 'http://127.0.0.1:8000/api/weekdays/hijri'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

