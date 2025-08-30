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
driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")

# 3. Click on Simple Alert button
simple_alert_btn = driver.find_element(By.ID, "alertBtn")
simple_alert_btn.click()

time.sleep(5)

# 4. Switch to the alert present and click on OK
driver.switch_to.alert.accept()

# 5. Click on Confirmation Alert button
confirmation_alert_btn = driver.find_element(By.ID, "confirmBtn")
confirmation_alert_btn.click()

time.sleep(5)

'''
# 6. Switch to the alert present and click on OK
driver.switch_to.alert.accept()
'''

# 6. Switch to the alert present and click on Cancel
driver.switch_to.alert.dismiss()

# 7. Click on Prompt Alert button
prompt_alert_btn = driver.find_element(By.ID, "promptBtn")
prompt_alert_btn.click()

time.sleep(5)

# 8. Enter text in the alert and click on OK
driver.switch_to.alert.send_keys("Vivek")
driver.switch_to.alert.accept()


