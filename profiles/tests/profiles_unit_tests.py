from django.test import TestCase
from django.contrib.auth.models import User

from profiles.models import Profile


class ProfileTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username="Josh", first_name="Josh", last_name="Lobio")
        Profile.objects.create(user=user, favorite_city="Paris")

    def test_profile(self):
        profile = Profile.objects.all().first()
        self.assertEqual(profile.user.username, "Josh")
