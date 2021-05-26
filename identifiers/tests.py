from django.test import TestCase, Client
from django.urls import reverse, resolve
from identifiers.views import IdentifiersView
from identifiers.models import Identifier
from datetime import datetime


def convert_date_str(date_time_str):
    return datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S.%f")


# Create your tests here.
class TestUrl(TestCase):

    def setUp(self):
        self.client = Client()

        self.sample_identifier = Identifier.objects.create()

    def test_api_identifiers_url_resolves(self):
        url = reverse('identifiers')
        self.assertEquals(resolve(url).func.view_class, IdentifiersView)

    def test_get_identifiers_endpoint(self):
        response = self.client.get(reverse('identifiers'))
        date_time_strings = list(response.data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(response.data), 2)
        self.assertGreater(convert_date_str(date_time_strings[0]), convert_date_str(date_time_strings[1]))
