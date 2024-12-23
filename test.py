from selenium import webdriver
from time import sleep

# Testing the selenium installation
browser = webdriver.Chrome()
browser.get('http://selenium.dev/')
browser.maximize_window()


# Add a delay to keep the brower open
sleep(10)