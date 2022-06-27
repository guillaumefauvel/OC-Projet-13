from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from django.urls import reverse, resolve

from oc_lettings_site.models import Address
from oc_lettings_site.views import index
import lettings.views
import profiles.views
from profiles.models import Profile
from lettings.models import Letting


class AdressTestCase(TestCase):
    """ Create an Adress object and check his presence """

    def setUp(self):
        Address.objects.create(number=1, street="Saint Georges Avenue", city="London",
                               state="London", zip_code="5208", country_iso_code="GBR")

    def test_adress(self):
        adress = Address.objects.get(street="Saint Georges Avenue")
        self.assertEqual(adress.zip_code, 5208)


class UrlTester(TestCase):
    """ Check the response status code and if the title contains the expected string """

    def setUp(self):
        user = User.objects.create(username="Josh", first_name="Josh", last_name="Lobio")
        Profile.objects.create(user=user, favorite_city="Paris")

        address = Address.objects.create(number=1, street="Saint Georges Avenue", city="London",
                                         state="London", zip_code="5208", country_iso_code="GBR")
        Letting.objects.create(title="London Paradise", address=address)

        self.c = Client()

    def test_index(self):
        response = self.c.get(reverse('index'))
        resolved_url = resolve(reverse('index'))
        
        assert resolved_url.func == index
        assert response.status_code == 200
        assert "<title>Holiday Homes</title>" in str(response.content)

    def test_profile_index(self):
        response = self.c.get(reverse('profiles_index'))
        resolved_url = resolve(reverse('profiles_index'))
        
        assert resolved_url.func == profiles.views.index
        assert response.status_code == 200
        assert "<title>Profiles</title>" in str(response.content)

    def test_profile_object(self):
        response = self.c.get(reverse('profile', args=['Josh']))
        resolved_url = resolve(reverse('profile', args=['Josh']))
        
        assert resolved_url.func == profiles.views.profile
        assert "<title>Josh</title>" in str(response.content)
        assert response.status_code == 200

    def test_letting_index(self):
        response = self.c.get(reverse('lettings_index'))
        resolved_url = resolve(reverse('lettings_index'))
        
        assert resolved_url.func == lettings.views.index        
        assert response.status_code == 200
        assert "<title>Lettings</title>" in str(response.content)

    def test_letting_object(self):
        response = self.c.get(reverse('letting', args=[1]))
        resolved_url = resolve(reverse('letting', args=[1]))
        assert resolved_url.func == lettings.views.letting        
        assert "<title>London Paradise</title>" in str(response.content)
        assert response.status_code == 200
