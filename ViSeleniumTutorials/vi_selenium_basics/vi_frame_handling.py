'''
Created on 30-Aug-2025

@author: admin
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. Lauching Chrome Browser with desired capabilities
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

# 2. Navigating to practice site
driver.get("https://demo.automationtesting.in/Frames.html")

# 3. Switch to single iframe
driver.switch_to.frame("SingleFrame")

# 4. Enter text in input text box
single_iframe_input = driver.find_element(By.TAG_NAME, "input")
single_iframe_input.send_keys("Vivek")

# 5. Switch to default content
driver.switch_to.default_content()

# 6. Click on "Iframe with in an Iframe"
iframe_within_iframe = driver.find_element(By.PARTIAL_LINK_TEXT, 'Iframe with in an Iframe')
iframe_within_iframe.click()

# 7. Switch to outer frame
driver.switch_to.frame(1)

# 8. Switch to inner frame
driver.switch_to.frame(0)

# 9. Enter text
multiple_iframe_input = driver.find_element(By.TAG_NAME, "input")
multiple_iframe_input.send_keys("Vivek")
