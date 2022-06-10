from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User

from oc_lettings_site.models import Address
from profiles.models import Profile
from lettings.models import Letting

class AdressTestCase(TestCase):
    
    def setUp(self):
        Address.objects.create(number=1, street="Saint Georges Avenue", city="London",
                               state="London", zip_code="5208", country_iso_code="GBR")

    def test_adress(self):
        adress = Address.objects.get(street="Saint Georges Avenue")
        self.assertEqual(adress.zip_code, 5208)


class UrlTester(TestCase):
    
    def setUp(self):
        user = User.objects.create(username="Josh", first_name="Josh", last_name="Lobio")
        Profile.objects.create(user=user, favorite_city="Paris")
        
        address = Address.objects.create(number=1, street="Saint Georges Avenue", city="London",
                               state="London", zip_code="5208", country_iso_code="GBR")
        letting = Letting.objects.create(title="London Paradise", address=address)
        
        self.c = Client()
        
    def test_index(self):
        response = self.c.get('/')
        assert response.status_code == 200
        assert "<title>Holiday Homes</title>" in str(response.content)
        
    def test_profile_index(self):
        response = self.c.get('/profiles/')
        assert response.status_code == 200
        assert "<title>Profiles</title>" in str(response.content)
        
    def test_profile_object(self):
        # TODO : To modify
        response = self.c.get('/profiles/Josh')
        assert response.status_code == 301
        
    def test_letting_index(self):
        response = self.c.get('/lettings/')
        assert response.status_code == 200
        assert "<title>Lettings</title>" in str(response.content)

    def test_letting_index(self):
        # TODO : To modify
        response = self.c.get('/lettings/1')
        assert response.status_code == 301
