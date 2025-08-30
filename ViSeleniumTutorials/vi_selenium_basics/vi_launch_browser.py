'''
Created on 15-Aug-2025

@author: admin
'''
from selenium import webdriver
from selenium.webdriver.common.by import By


# 1. Lauching Chrome Browser with desired capabilities
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)
# driver = webdriver.Edge()

# 2. Navigating to practice site
driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")

# 3. Enter name
# Locating
name_txt_bx = driver.find_element(By.CSS_SELECTOR, '#name')

# Action
name_txt_bx.send_keys("Vivek")

# 4. Click on male radio button
# Locating
male_radio_button = driver.find_element(By.ID, "male")
#Action
male_radio_button.click()

'''
"/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[1]/div[1]/div/div/div/div/div[2]/div[1]/input[1]"
'//*[@id="name"]'

'//*[@id="HTML4"]/div[1]/button'
'//button[@onclick="myFunction()"]'
'//div[@data="//button[normalize-space()='Checkout here'][@class='dropbtn']"]'
'''
