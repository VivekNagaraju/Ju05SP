'''
Created on 31-Aug-2025

@author: admin
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


# 1. Lauching Chrome Browser with desired capabilities
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

# 2. Navigating to practice site
driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")

# 3. Locate the <select> tag element
country_drop_down = driver.find_element(By.ID, "country")

# 4. Create a Select class object
select_country = Select(country_drop_down)

# 5. Select country by index
select_country.select_by_index(4)

time.sleep(3)

# 6. Deselect
# select_country.deselect_by_index(4) # deselect only works for drop downs which support multiple selections

# 7. Select country by value
select_country.select_by_value('uk')

time.sleep(3)

# 8. Deselect
# select_country.deselect_by_value('uk')

# 9. Select country by visible text
select_country.select_by_visible_text("China")
