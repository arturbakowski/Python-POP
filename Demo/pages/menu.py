from locators.locators import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from pages.base import BasePage


class Menu(BasePage):

    # MENU
    def click_home(self):
        self.click_button(*MainPageLocators.MENU_HOME)

    def click_about_us(self):
        self.click_button(*MainPageLocators.MENU_ABOUT_US)

    def click_services(self):
        self.click_button(*MainPageLocators.MENU_SERVICES)

    def click_demo(self):
        self.click_button(*MainPageLocators.MENU_DEMO)

    def click_blog(self):
        self.click_button(*MainPageLocators.MENU_BLOG)

    def click_contact(self):
        self.click_button(*MainPageLocators.MENU_CONTACT)

    # RIGHT MENU
    def click_registration(self):
        self.click_button(*MainPageLocators.REGISTRATION_BUTTON)

    def click_draggable(self):
        self.click_button(*MainPageLocators.DRAGGABLE_BUTTON)
