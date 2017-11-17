import unittest
import time
from selenium import webdriver
import sys
sys.path.append('../pages')
sys.path.append('../resources')
from contact import *
import resources

class TestContactPage(unittest.TestCase):
    """A test class of the page object pattern"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(resources.app_link)
        self.driver.implicitly_wait(5)  # seconds
      #  self.driver.get_screenshot_as_file('results/' + 'screen.jpg')

    def test_contact_page(self):
        """Contact Page Verification"""
        contact = ContactPage(self.driver)
        contact.click_contact()
        assert "Contact" in self.driver.page_source

        contact.fill_name(resources.get_first_name())
        contact.fill_email(resources.get_email())
        contact.fill_subject("subject")
        contact.fill_message("message")
        contact.click_send()
        time.sleep(5)

        assert "Your message was sent successfully. Thanks." \
               in self.driver.page_source

    def tearDown(self):
        self.driver.quit()
        #self.driver.close()


if __name__ == "__main__":
    unittest.main()