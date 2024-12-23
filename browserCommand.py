from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Trying out different browser commands
browser = webdriver.Chrome()
browser.get("https://opensource-demo.orangehrmlive.com/")
browser.maximize_window()
sleep(5)
# browser.minimize_window()
# browser.fullscreen_window()

# browser move forward by going to another screen
browser.find_element(By .CSS_SELECTOR, value=".oxd-text.oxd-text--p.orangehrm-login-forgot-header").click()
sleep(5)

browser.back() # go backard
sleep(5)

browser.forward() # go forward
sleep(5)

browser.refresh() # refresh the page

# Sleep for longer display
sleep(10)

# closing the browser
browser.close()