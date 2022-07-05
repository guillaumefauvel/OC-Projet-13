import platform
import os

from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User
from selenium.webdriver.common.by import By
from selenium import webdriver

from oc_lettings_site.models import Address
from lettings.models import Letting
from profiles.models import Profile


class functionnal_tests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        print('-'*70)
        print('\n- Start of functionnal tests -\n')
        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument("--no-sandbox")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument('--headless')
        if platform.system() == 'Windows':
            cls.driver = webdriver.Chrome('dependencies/win_chromedriver.exe', chrome_options=options)
        if platform.system() == 'Linux':
            permission_id = '0755'
            os.chmod('dependencies/linux_chromedriver', int(permission_id, base=8))
            cls.driver = webdriver.Chrome('dependencies/linux_chromedriver', chrome_options=options)
        cls.driver.implicitly_wait(10)
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        super().tearDownClass()
    
    def populate_db(self):
        
        user = User.objects.create(username="Josh", first_name="Josh", last_name="Lobio")
        Profile.objects.create(user=user, favorite_city="Paris")

        address = Address.objects.create(number=1, street="Saint Georges Avenue", city="London",
                                         state="London", zip_code="5208", country_iso_code="GBR")
        Letting.objects.create(title="London Paradise", address=address)
        
    def main_page(self):
        self.populate_db()
        self.BASE_URL = self.live_server_url
        self.driver.get(self.BASE_URL + reverse('index'))

    def test_profile_object(self):
        self.main_page()
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Profiles').click()
        assert self.driver.current_url == self.BASE_URL + reverse('profiles_index')
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Josh').click()
        assert self.driver.current_url == self.BASE_URL + reverse('profile', args=['Josh'])

    def test_lettings_object(self):
        self.main_page()
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Lettings').click()
        assert self.driver.current_url == self.BASE_URL + reverse('lettings_index')
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value='London Paradise').click()
        assert self.driver.current_url == self.BASE_URL + reverse('letting', args=[4])
    
    def test_home_button_from_lettings(self):
        self.main_page()
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Lettings').click()
        assert self.driver.current_url == self.BASE_URL + reverse('lettings_index')
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Home').click()
        assert self.driver.current_url == self.BASE_URL + reverse('index')

    def test_profiles_button_from_lettings(self):
        self.main_page()
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Lettings').click()
        assert self.driver.current_url == self.BASE_URL + reverse('lettings_index')
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Profiles').click()
        assert self.driver.current_url == self.BASE_URL + reverse('profiles_index')

    def test_home_button_from_profiles(self):
        self.main_page()
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Profiles').click()
        assert self.driver.current_url == self.BASE_URL + reverse('profiles_index')
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Home').click()
        assert self.driver.current_url == self.BASE_URL + reverse('index')

    def test_lettings_button_from_profiles(self):
        self.main_page()
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Profiles').click()
        assert self.driver.current_url == self.BASE_URL + reverse('profiles_index')
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Lettings').click()
        assert self.driver.current_url == self.BASE_URL + reverse('lettings_index')