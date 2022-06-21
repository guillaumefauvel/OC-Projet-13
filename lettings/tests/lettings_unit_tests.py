from django.test import TestCase

from oc_lettings_site.models import Address
from lettings.models import Letting


class LettingsTestCase(TestCase):

    def setUp(self):
        self.address = Address.objects.create(number=1, street="Saint Georges Avenue", city="London",
                                         state="London", zip_code="5208", country_iso_code="GBR")
        self.letting = Letting.objects.create(title="London Paradise", address=self.address)

    def test_profile(self):

        self.assertEqual(self.letting.address.street, "Saint Georges Avenue")
