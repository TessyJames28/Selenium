from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep


url = "https://the-internet.herokuapp.com/drag_and_drop"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

# Identify element to be dragged and dropped
source_element = browser.find_element(By .ID, value="column-a") #Drag this element
destination_element = browser.find_element(By .ID, value="column-b") # Drop here

#Drag and drop
actions = ActionChains(browser)
actions.drag_and_drop(source_element, destination_element).perform()
sleep(5)
