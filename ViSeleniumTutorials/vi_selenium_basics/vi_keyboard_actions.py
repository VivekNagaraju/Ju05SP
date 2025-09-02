'''
Created on 02-Sep-2025

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

# 3. Create ActionChains object
actions = ActionChains(driver)

# 4. Copy text from Field1 using Keyboard actions 

# Ctrl+a 
field1 = driver.find_element(By.ID, 'field1')
actions.key_down(Keys.CONTROL, field1).send_keys('a').key_up(Keys.CONTROL).perform()

# Ctrl+c
actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

# 5. Paste the text into Field2 using Keyboard actions--> Ctrl+v

field2 = driver.find_element(By.ID, 'field2')
actions.key_down(Keys.CONTROL, field2).send_keys('v').key_up(Keys.CONTROL).perform()