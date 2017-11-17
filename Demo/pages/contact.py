import sys
sys.path.append('../locators')
sys.path.append('../pages')
from base import BasePage
# noinspection PyUnresolvedReferences
from locators import ContactLocators
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select


class ContactPage(BasePage):

    def fill_name(self, name):
        self.fill_input(name, *ContactLocators.NAME)

    def fill_email(self, email):
        self.fill_input(email, *ContactLocators.EMAIL)

    def fill_subject(self, subject):
        self.fill_input(subject, *ContactLocators.SUBJECT)

    def fill_message(self, message):
        self.fill_input(message, *ContactLocators.MESSAGE)

    def click_send(self):
        self.click_button(*ContactLocators.SEND)

