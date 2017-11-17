import sys
sys.path.append('../locators')
sys.path.append('../pages')
from base import BasePage
# noinspection PyUnresolvedReferences
from locators import RegistrationLocators
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class RegistrationPage(BasePage):

    def fill_first_name(self, name):
        self.fill_input(name, *RegistrationLocators.FIRST_NAME)

    def fill_last_name(self, name):
        self.fill_input(name, *RegistrationLocators.LAST_NAME)

    def check_dance(self):
        self.click_button(*RegistrationLocators.HOBBY_DANCE)

    def check_reading(self):
        self.click_button(*RegistrationLocators.HOBBY_READING)

    def check_cricket(self):
        self.click_button(*RegistrationLocators.HOBBY_CRICKET)

    def select_country(self, value):
        select = Select(self.find_element(*RegistrationLocators.COUNTRY))
        select.select_by_value(value)

    def fill_phone(self, number):
        self.fill_input(number, *RegistrationLocators.PHONE_NUMBER)

    def fill_username(self, user):
        self.fill_input(user, *RegistrationLocators.USERNAME)

    def fill_email(self, email):
        self.fill_input(email, *RegistrationLocators.EMAIL)

    def fill_password(self, password):
        self.fill_input(password, *RegistrationLocators.PASSWORD)

    def fill_confirm_password(self, password):
        self.fill_input(password, *RegistrationLocators.CONFIRM_PASSWORD)

    def click_submit(self):
        self.click_button(*RegistrationLocators.SUBMIT)
