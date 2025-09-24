'''
Created on 24-Sep-2025

@author: admin
'''
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'Chrome browser is launched')
def launch_chrome_browser(context):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("start-maximized")
    context.driver = webdriver.Chrome(options=options)
    context.driver.implicitly_wait(5)


@when(u'User navigates to OrangeHRM Login Page')
def navigate_to_login_page(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@then(u'User should see page title as OrangeHRM')
def validate_login_page_title(context):
    expected_title = "OrangeHRM"
    actual_title = context.driver.title
    assert actual_title == expected_title, "Page title is not matching"