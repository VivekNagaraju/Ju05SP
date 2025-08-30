'''
Created on 30-Aug-2025

@author: admin
'''
from selenium import webdriver
from selenium.webdriver.common.by import By


# 1. Lauching Chrome Browser with desired capabilities
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

# 2. Navigating to practice site
driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")

# 3. Wiki search
wiki_search_txt_box = driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input")
wiki_search_txt_box.send_keys("Software Testing")

wiki_search_button = driver.find_element(By.CLASS_NAME, "wikipedia-search-button")
wiki_search_button.click()

# 4. Click on result link
result_link = driver.find_element(By.LINK_TEXT, "Software testing")
result_link.click()

print("driver.window_handles-->", driver.window_handles)
print("driver.current_window_handle-->", driver.current_window_handle)
print("driver.title-->", driver.title)

window_handles_list = driver.window_handles

driver.switch_to.window(window_handles_list[1])


print("==========After Tab Switch==============")
print("driver.current_window_handle-->", driver.current_window_handle)
print("driver.title-->", driver.title)


# 5. Click on "correctness" link in new tab
result_linkone = driver.find_element(By.LINK_TEXT, "correctness")
result_linkone.click()

