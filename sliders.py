from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep


url = "https://the-internet.herokuapp.com/horizontal_slider"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

# Find the slider by using/creating an XPATh for the range
slider = browser.find_element(By .XPATH, value="//input[@type='range']")

#Action chain for sliding
actions = ActionChains(browser)

# the click_and_hold, clicks and hold the slider, mover by offset then moves it per given range
# relase then releases the slider and perform gives it the command to perform the action
actions.click_and_hold(slider).move_by_offset(xoffset=50, yoffset=0).release().perform()
sleep(5)