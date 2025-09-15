'''
Created on 15-Sep-2025

@author: admin
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestOrangeHRMLoginPage(unittest.TestCase):


    def test_navigation_to_orangehrm_login_page(self):
        # 1. Lauching Chrome Browser with desired capabilities
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("start-maximized")
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(5)
        
        # 2. Navigating to OrangeHRM Login Page
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        
        # 3. Validating the page title
        expected_title = "OrangeHRM1"
        actual_title = driver.title
        self.assertEqual(actual_title, expected_title, "Page title is not matching")
        
        # 4. Validating the page url
        expected_url_portion = "/auth/login"
        actual_url = driver.current_url
        self.assertIn(expected_url_portion, actual_url, "Current page URL doesn't contain '/auth/login'")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()