from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Explicit Wait: To use an explicit wait which allows to spacify a wait condition
# create a WebDriverWait object from selenium.webdriver.support.ui.WebDriverWait
# Use expected conditions from selenium.webdriver.support.expected_conditions

url = "https://www.saucedemo.com/"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

browser.find_element(By .ID, value="user-name").send_keys('standard_user')
browser.find_element(By .ID, value="password").send_keys('secret_sauce')
browser.find_element(By .ID, value="login-button").click()

# Handle logout for each of the login
browser.find_element(By .XPATH, value="//button[@id='react-burger-menu-btn']").click()

# Create the explicit wait, pass the driver and use util to indicate the condition
element = WebDriverWait(browser, timeout=10).until(EC.element_to_be_clickable((By .XPATH, "//a[@id='logout_sidebar_link']")))
# browser.find_element(By .XPATH, value="//a[@id='logout_sidebar_link']").click()
#The above line will now be replaced by element.click()
element.click()