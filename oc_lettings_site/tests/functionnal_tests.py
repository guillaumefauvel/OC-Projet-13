from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import unittest


class FunctionnalTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.headless = False
        cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def main_page(self):
        self.driver.get('http://127.0.0.1:8000')
        
    def test_profile_object(self):
        self.main_page()
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value="Profiles").click()
        assert self.driver.current_url == 'http://127.0.0.1:8000/profiles/'
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value="HeadlinesGazer").click()
        assert self.driver.current_url == 'http://127.0.0.1:8000/profiles/HeadlinesGazer/'
        
    def test_lettings_object(self):
        self.main_page()
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value="Lettings").click()
        assert self.driver.current_url == 'http://127.0.0.1:8000/lettings/'
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value="Joshua Tree Green Haus").click()
        assert self.driver.current_url == 'http://127.0.0.1:8000/lettings/1/'

    def test_home_button_from_lettings(self):
        self.main_page()
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value="Lettings").click()
        assert self.driver.current_url == 'http://127.0.0.1:8000/lettings/'
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value="Home").click()
        assert self.driver.current_url == 'http://127.0.0.1:8000/'

    def test_profiles_button_from_lettings(self):
        self.main_page()
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value="Lettings").click()
        assert self.driver.current_url == 'http://127.0.0.1:8000/lettings/'
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value="Profiles").click()
        assert self.driver.current_url == 'http://127.0.0.1:8000/profiles/'

    def test_home_button_from_profiles(self):
        self.main_page()
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value="Profiles").click()
        assert self.driver.current_url == 'http://127.0.0.1:8000/profiles/'
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value="Home").click()
        assert self.driver.current_url == 'http://127.0.0.1:8000/'

    def test_lettings_button_from_profiles(self):
        self.main_page()
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value="Profiles").click()
        assert self.driver.current_url == 'http://127.0.0.1:8000/profiles/'
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value="Lettings").click()
        assert self.driver.current_url == 'http://127.0.0.1:8000/lettings/'

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('\n\n- End of functionnal tests -')


if __name__ == '__main__':
    unittest.main()