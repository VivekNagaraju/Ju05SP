'''
Created on 01-Sep-2025

@author: admin
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

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

# 4. Scrolling
actions.scroll_by_amount(0, 1000).perform()

# 4. Mouse Hover on Point me
point_me_btn = driver.find_element(By.CLASS_NAME, 'dropbtn')
actions.move_to_element(point_me_btn)

time.sleep(3)

# 5. Double click on Copy Text button
copy_text_btn = driver.find_element(By.XPATH, "//button[text()='Copy Text']")
actions.double_click(copy_text_btn)
actions.perform()