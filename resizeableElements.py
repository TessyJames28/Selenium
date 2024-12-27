from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep


url = "https://demo.automationtesting.in/Resizable.html"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

# Grabbing the resizable point
resizable_element = browser.find_element(By .XPATH, value="//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
#Get initial size
initial_element_size = browser.find_element(By .XPATH, value="//div[@id='resizable']")

# Get inital height and width
inital_size = initial_element_size.size # Get the size of the inital element
print(f"Initial size: {inital_size}")
sleep(5)

#Create action chain to handling sliding action
actions = ActionChains(browser)

# the click_and_hold, clicks and hold the slider, mover by offset then moves it per given range
# relase then releases the slider and perform gives it the command to perform the action
actions.click_and_hold(resizable_element).move_by_offset(xoffset=100, yoffset=100).release().perform()
sleep(5)
resized_element = initial_element_size.size # Get the new size after resizing
print(f"Resized element: {resized_element}")
