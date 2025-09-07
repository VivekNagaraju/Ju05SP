'''
Created on 07-Sep-2025

@author: admin
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys

# 1. Lauching Chrome Browser with desired capabilities
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

# 2. Navigating to practice site
driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")

# 3. Locate the shadow host
shadow_host = driver.find_element(By.ID, 'shadow_host')

# 4. Get the shadow root
first_shadow_root = shadow_host.shadow_root

# 5. Locate the element in shadow DOM using shadow root --> input text box
shadow_input_txtbox = first_shadow_root.find_element(By.CSS_SELECTOR, "input[type=text]:nth-child(5)")
# print(shadow_input_txtbox)
shadow_input_txtbox.send_keys("Vivek")

# 6. Get 'Mobiles' text
span = first_shadow_root.find_element(By.CSS_SELECTOR, '#shadow_content > span')
print(span.text)