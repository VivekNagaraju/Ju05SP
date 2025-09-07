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

# 3. Locate Datepicker2
date_picker2 = driver.find_element(By.ID, 'txtDate')

'''
# 4. Remove readonly attribute from date_picker2
driver.execute_script("arguments[0].removeAttribute('readonly');", date_picker2)

# 5. Enter date in date_picker2
date_picker2.send_keys("13/09/2025")
'''

# 4. Enter date in date_picker2 using script
driver.execute_script("arguments[0].value = arguments[1];", date_picker2, "13/09/2025")