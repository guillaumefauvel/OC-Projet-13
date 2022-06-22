from django.test import TestCase
from django.urls import reverse
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from oc_lettings_site.models import Address
from lettings.models import Letting


class test_lettings(TestCase):

    def setUp(self):
        self.address = Address.objects.create(number=1, street='Saint Georges Avenue',
                                              city='London', state='London', zip_code='5208',
                                              country_iso_code='GBR')
        self.letting = Letting.objects.create(title='London Paradise', address=self.address)

    def test_profile(self):

        print(reverse('index'))

        self.assertEqual(self.letting.address.street, 'Saint Georges Avenue')


class test_functionnal(TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('-'*70)
        print('\n- Start of functionnal tests -\n')
        options = webdriver.ChromeOptions()
        options.headless = True
        #  cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        #  ChromeDriver V-102.0.5005.61
        cls.driver = webdriver.Chrome('dependencies/chromedriver.exe', options=options)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

    def main_page(self):
        self.BASE_URL = 'http://localhost:8000'
        self.driver.get(self.BASE_URL + reverse('index'))

    def test_profile_object(self):
        self.main_page()
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Profiles').click()
        assert self.driver.current_url == self.BASE_URL + reverse('profiles_index')
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value='HeadlinesGazer').click()
        assert self.driver.current_url == self.BASE_URL + reverse('profile', args=['HeadlinesGazer'])

    def test_lettings_object(self):
        self.main_page()
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Lettings').click()
        assert self.driver.current_url == self.BASE_URL + reverse('lettings_index')
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Joshua Tree Green Haus').click()
        assert self.driver.current_url == self.BASE_URL + reverse('letting', args=[1])

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


