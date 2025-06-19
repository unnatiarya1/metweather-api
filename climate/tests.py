from django.test import TestCase
from .models import ClimateData

class ClimateModelTest(TestCase):
    def test_create_data(self):
        data = ClimateData.objects.create(region='UK', parameter='Tmax', year=2022, month=5, value=17.4)
        self.assertEqual(data.value, 17.4)

