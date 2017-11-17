# noinspection PyUnresolvedReferences
from locators import MainPageLocators

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def fill_input(self, value, *locator):
        elem = self.find_element(*locator)
        elem.send_keys(value)

    def click_button(self, *locator):
        self.find_element(*locator).click()

    def navigate(self, url):
        self.driver.get(self.url)

    # MENU
    def click_home(self):
        self.click_button(*MainPageLocators.MENU_HOME)

    def click_about_us(self):
        self.click_button(*MainPageLocators.MENU_ABOUT_US)

    def click_services(self):
        self.click_button(*MainPageLocators.MENU_SERVICES)

    def click_demo(self):
        self.click_button(*MainPageLocators.MENU_DEMO)

    def click_demo_draggable(self):
        self.click_button(*MainPageLocators.MENU_DEMO_DRAGGABLE)

    def click_demo_tabs(self):
        self.click_button(*MainPageLocators.MENU_DEMO_TABS)

    def click_blog(self):
        self.click_button(*MainPageLocators.MENU_BLOG)

    def click_contact(self):
        self.click_button(*MainPageLocators.MENU_CONTACT)

    # RIGHT MENU
    def click_registration(self):
        self.click_button(*MainPageLocators.REGISTRATION_BUTTON)

    def click_draggable(self):
        self.click_button(*MainPageLocators.DRAGGABLE_BUTTON)