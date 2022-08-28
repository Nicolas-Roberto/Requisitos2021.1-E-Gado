from rest_framework import status
from rest_framework.test import APITestCase

from backend.egado_app.ration_farm.serializers import RationFarmSerializer
from .models import RationFarm
from rest_framework.test import APITestCase

#from backend.egado_app.ration_farm.models import RationFarm

# Create your tests here.
class RationFarmTestCase(APITestCase):

    url = 'http://localhost:8000/' + 'ration_farm/'
    rationFarmUrl = '/ration_farm/'

    def setUp(self):
        self.rationFarm1 = RationFarm.objects.create(
            name='Ração A+', preco = 100, quantidade = 50
        )

    def testPost(self):
        data = {
            'name': self.rationFarm1.name,
            'preco': self.rationFarm1.preco,
            'quantidade':self.rationFarm1.quantidade
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


