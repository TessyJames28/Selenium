from selenium import webdriver
from time import sleep


# Handling basic auth with no htnl element to identify attributes to use and automate the process
# To handle the certification, you take the format below as shown on url
# https://username:password@domain/path
url = "https://admin:admin@the-internet.herokuapp.com/basic_auth"
username = "admin" # User name for login
password = "admin"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
sleep(5)