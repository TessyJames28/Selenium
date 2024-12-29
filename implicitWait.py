from selenium import webdriver
from selenium.webdriver.common.by import By


# Implicit wait
url = "https://www.saucedemo.com/"
browser = webdriver.Chrome()
# With implicit wait, the default is 0 and is applicable for all driver element
# The given time is maximum amount of tim driver will wait before throwing an error
browser.implicitly_wait(10)
browser.maximize_window()
browser.get(url)

browser.find_element(By .ID, value="user-name").send_keys('standard_user')
browser.find_element(By .ID, value="password").send_keys('secret_sauce')
browser.find_element(By .ID, value="login-button").click()


# Handle logout for each of the login
browser.find_element(By .XPATH, value="//button[@id='react-burger-menu-btn']").click()
browser.find_element(By .XPATH, value="//a[@id='logout_sidebar_link']").click()
