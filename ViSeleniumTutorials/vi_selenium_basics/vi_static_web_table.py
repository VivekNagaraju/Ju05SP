'''
Created on 05-Sep-2025

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

# 3. Get text from a static web table cell
table_cell = driver.find_element(By.XPATH, '//table[@name="BookTable"]/tbody/tr[2]/td[1]')
table_cell_value = table_cell.text
print(table_cell_value)

'''
//td[contains(text(),'Mbps')]
//td[contains(text(),'MB') and not(contains(text(), '/s'))]
//*[@id="rows"]/tr[1]/td[1]//following-sibling::td[contains(text(),'Mbps')]
'''