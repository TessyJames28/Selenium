from selenium import webdriver
from time import sleep

# Testing the selenium installation
browser = webdriver.Chrome()
browser.get('http://selenium.dev/')
browser.maximize_window()

# Check the title
title = browser.title
print(title)

# Test that the title is correct
assert "Selenium" in title

# Test what happens with the wrong title
assert "Selenium123" in title

# Add a delay to keep the brower open
sleep(10)