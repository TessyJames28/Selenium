from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url = "https://www.selenium.dev/"
url2 = "https://playwright.dev/"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

# Switching to new window to open the second url
browser.switch_to.new_window()
browser.get(url2)

# Count number of tabs
num_of_tab = len(browser.window_handles)
print(num_of_tab)

# Getting the value of tabs
tab_value = browser.window_handles
print(tab_value)

# Get the value of the current browser
current_tab = browser.current_window_handle
print(current_tab)
browser.find_element(By .CSS_SELECTOR, value=".getStarted_Sjon").click()
sleep(3)

# Switching to first tab to perform some actions accordingly
firstTab = browser.window_handles[0]
if current_tab != firstTab:
    browser.switch_to.window(firstTab)
    sleep(2)

browser.find_element(By .XPATH, value="//span[normalize-space()='Downloads']").click()
sleep(3)