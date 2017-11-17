import sys
sys.path.append('../locators')
sys.path.append('../pages')
from base import BasePage
# noinspection PyUnresolvedReferences
from locators import MainPageLocators
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select


class MainPage(BasePage):

    #HOME CONTENT
    def click_left_image(self):
        self.click_button(*MainPageLocators.LEFT_IMAGE)

    def click_center_image(self):
        self.click_button(*MainPageLocators.CENTER_IMAGE)

    #TABS
    def click_first_tab(self):
        self.click_button(*MainPageLocators.FIRST_TAB)

    def click_second_tab(self):
        self.click_button(*MainPageLocators.SECOND_TAB)

    #TABS CONTENT
    def get_first_tab(self):
        tab = self.find_element(*MainPageLocators.Tab_1)
        return tab.text

    def get_second_tab(self):
        tab = self.find_element(*MainPageLocators.Tab_2)
        return tab.text
