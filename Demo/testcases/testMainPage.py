import unittest
from selenium import webdriver
import sys
sys.path.append('../pages')
from main_page import *
import time


class TestMainPage(unittest.TestCase):
    """A test class of the page object pattern"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://demoqa.com')
        self.driver.implicitly_wait(5)  # seconds
      #  self.driver.get_screenshot_as_file('results/' + 'screen.jpg')

    def test_main_page(self):
        """Main Page Verification"""
        main_page = MainPage(self.driver)
        main_page.click_home()
        assert "Demoqa" in self.driver.title

        main_page.click_about_us()
        assert "About us" in self.driver.title

        main_page.click_services()
        assert "Services" in self.driver.title

        main_page.click_demo()
        main_page.click_demo_draggable()
        assert "Draggable" in self.driver.title

        main_page.click_demo()
        main_page.click_demo_tabs()
        assert "Tabs" in self.driver.title

        main_page.click_blog()
        assert "Blog" in self.driver.title

        main_page.click_contact()
        assert "Contact" in self.driver.title

        main_page.click_home()
        assert "Demoqa" in self.driver.title
        self.assertNotEqual(main_page.get_first_tab(), main_page.get_second_tab())
        self.assertEqual(main_page.get_first_tab(), 'Content 1 Title')
        self.assertNotEqual(main_page.get_first_tab(), 'Content 2 Title')
        print('PRINT 1 ' + main_page.get_first_tab())

        main_page.click_second_tab()
        self.assertEqual(main_page.get_second_tab(), 'Content 2 Title')
        self.assertNotEqual(main_page.get_second_tab(), 'Content 1 Title')
        print('PRINT 2 ' + main_page.get_second_tab())
        print('PRINT 3 ' + main_page.get_first_tab())

        main_page.click_first_tab()
        self.assertEqual(main_page.get_first_tab(), 'Content 1 Title')
        self.assertNotEqual(main_page.get_first_tab(), 'Content 2 Title')
        print('PRINT 4 ' + main_page.get_first_tab())
        print('PRINT 5 ' + main_page.get_second_tab())

        main_page.click_left_image()
        assert "pattern-14.png" in self.driver.title
        time.sleep(3)

        self.driver.back()
        assert "Demoqa" in self.driver.title
        main_page.click_center_image()
        assert "pattern-14.png" in self.driver.title
        time.sleep(3)

        self.driver.back()
        assert "Demoqa" in self.driver.title

    def tearDown(self):
        self.driver.quit()
        #self.driver.close()


if __name__ == "__main__":
    unittest.main()