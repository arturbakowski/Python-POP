from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for the Main Page locators. All main page locators should come here"""
    # Menu
    MENU_HOME = (By.ID, 'menu-item-38')
    MENU_ABOUT_US = (By.ID, 'menu-item-158')
    MENU_SERVICES = (By.ID, 'menu-item-155')
    MENU_DEMO = (By.ID, 'menu-item-66')
    MENU_DEMO_DRAGGABLE = (By.ID, 'menu-item-73')
    MENU_DEMO_TABS = (By.ID, 'menu-item-153')
    MENU_BLOG = (By.ID, 'menu-item-65')
    MENU_CONTACT = (By.ID, 'menu-item-64')
    # Right Menu
    REGISTRATION_BUTTON = (By.ID, 'menu-item-374')
    DRAGGABLE_BUTTON = (By.ID, 'menu-item-140')
    DROPPABLE_BUTTON = (By.ID, 'menu-item-141"')
    RESIZABLE_BUTTON = (By.ID, 'menu-item-143')
    SELECTABLE_BUTTON = (By.ID, 'menu-item-142')
    SORTABLE_BUTTON = (By.ID, 'menu-item-151')
    # Home Content
    LEFT_IMAGE = (By.XPATH, "//*[@id='post-9']/div/div[1]/div/p[1]/a/img")
    CENTER_IMAGE = (By.CSS_SELECTOR, '#post-9 > div > div:nth-child(2) > div > p:nth-child(1) > i > a > img')
    RIGHT_IMAGE = (By.CLASS_NAME, 'alignnone.size-medium.wp-image-225')
    # Tabs
    FIRST_TAB = (By.ID, 'ui-id-1')
    SECOND_TAB = (By.ID, 'ui-id-2')
    THIRD_TAB = (By.ID, 'ui-id-3')
    FOURTH_TAB = (By.ID, 'ui-id-4')
    FIFTH_TAB = (By.ID, 'ui-id-5')
    # Tabs content
    Tab_1 = (By.CSS_SELECTOR, '#tabs-1 > b')
    Tab_2 = (By.XPATH, '//*[@id="tabs-2"]/b')

class RegistrationLocators(object):
    """A class for the Registration page locators. All registration page locators should come here"""
    FIRST_NAME = (By.ID, 'name_3_firstname')
    LAST_NAME = (By.ID, 'name_3_lastname')
    HOBBY_DANCE = (By.CSS_SELECTOR, '#pie_register > li:nth-child(3) > div > div > input:nth-child(2)')
    HOBBY_READING = (By.XPATH, "//*[@id='pie_register']/li[3]/div/div/input[2]")
    HOBBY_CRICKET = (By.XPATH, "//*[@id='pie_register']/li[3]/div/div/input[3]")
    COUNTRY = (By.ID, 'dropdown_7')
    PHONE_NUMBER = (By.ID, 'phone_9')
    USERNAME = (By.ID, 'username')
    EMAIL = (By.ID, 'email_1')
    PASSWORD = (By.ID, 'password_2')
    CONFIRM_PASSWORD = (By.ID, 'confirm_password_password_2')
    SUBMIT = (By.NAME, 'pie_submit')
    PASSWORD_STRENGTH = (By.ID, 'password_meter')


class ContactLocators(object):
    """A class for the Contact page locators. All contact page locators should come here"""
    NAME = (By.NAME, 'your-name')
    EMAIL = (By.NAME, 'your-email')
    SUBJECT = (By.CSS_SELECTOR, '#wpcf7-f375-p28-o1 > form > p:nth-child(4) > span > input')
    MESSAGE = (By.NAME, 'your-message')
    SEND = (By.XPATH, "//*[@id='wpcf7-f375-p28-o1']/form/p[5]/input")
