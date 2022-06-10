from django.test import TestCase

from oc_lettings_site.models import Address
from lettings.models import Letting


class LettingsTestCase(TestCase):
    
    def setUp(self):
        address = Address.objects.create(number=1, street="Saint Georges Avenue", city="London",
                               state="London", zip_code="5208", country_iso_code="GBR")
        letting = Letting.objects.create(title="London Paradise", address=address)

    def test_profile(self):
        letting = Letting.objects.all().first()

        self.assertEqual(letting.address.street, "Saint Georges Avenue")
        

