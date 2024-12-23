from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Automating Login
browser = webdriver.Chrome()
browser.maximize_window()

username = "standard_user"
password = "secret_sauce"
login_url = "http://saucedemo.com/"

# Getting the url, username, pasoword, and login button field
browser.get(login_url)
username_field = browser.find_element(By .ID, value="user-name")
password_field = browser.find_element(By .ID, value="password")
login_button = browser.find_element(By .ID, value="login-button")

# Adding the username and password
username_field.send_keys(username)
password_field.send_keys(password)

# Ensure the button is not disabled before clicking the login button
assert not login_button.get_attribute("disabled")
login_button.click()

#Test for successful login
success_element = browser.find_element(By .CSS_SELECTOR, value=".title")
assert success_element.text == "Products"

# Add a delay to keep the brower open
sleep(10)