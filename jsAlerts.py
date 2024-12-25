from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


url = "https://the-internet.herokuapp.com/javascript_alerts"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

# Click the alert button 
# alert_button = browser.find_element(By .XPATH, value="//button[normalize-space()='Click for JS Alert']")
# alert_button = browser.find_element(By .XPATH, value="//button[normalize-space()='Click for JS Confirm']")
alert_button = browser.find_element(By .XPATH, value="//button[normalize-space()='Click for JS Prompt']")
alert_button.click()
sleep(2)

# Get alert text by switching to the alert frame
alert = browser.switch_to.alert
alert_text = alert.text
print(f"Alert text is: {alert_text}")

# To handle alert
# alert.accept()

# Canceling an alert
# alert.dismiss()

#Handling alert that need text input
alert.send_keys("This is Selenium Python tutorial on handling alert")
alert.accept()
sleep(3)





