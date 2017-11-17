import sys
sys.path.append('../pages')
sys.path.append('../resources')
import unittest
import time
from selenium import webdriver
from registration import *
import resources


class TestRegistration(unittest.TestCase):
    """Test class of the page object pattern"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(resources.app_link)
        self.driver.implicitly_wait(5)  # seconds
      #  self.driver.get_screenshot_as_file('results/' + 'screen.jpg')

    def test_registration(self):
        """Simple registration test"""
        registration = RegistrationPage(self.driver)
        registration.click_registration()
        assert "Registration" in self.driver.title

        registration.fill_first_name(resources.get_first_name())
        registration.fill_last_name(resources.get_last_name())
        registration.check_dance()
        registration.check_reading()
        registration.check_cricket()
        registration.select_country('Poland')
        registration.fill_phone(resources.get_phone_number())
        time.sleep(5)
        registration.fill_username(resources.get_username())
        time.sleep(5)
        registration.fill_email(resources.get_email())

        password = resources.get_password()
        registration.fill_password(password)
        registration.fill_confirm_password(password)
        registration.click_submit()
        time.sleep(5)

        # basic assertion for unknown errors
        assert "Error" not in self.driver.page_source

        # assertion for successful registration
        assert "Thank you for your registration" in self.driver.page_source

    def tearDown(self):
        self.driver.quit()
        #self.driver.close()


if __name__ == "__main__":
    unittest.main()