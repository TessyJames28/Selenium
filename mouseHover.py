from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep


url = "https://demo.automationtesting.in/Datepicker.html"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

# create an object for Action chains to be used for mouse action
actions = ActionChains(browser)
#Target the element needed to hover over
hover_element = browser.find_element(By .XPATH, value="//a[normalize-space()='SwitchTo']")
actions.move_to_element(hover_element).perform() # Hover over the element
sleep(3)
browser.find_element(By .CSS_SELECTOR, value="a[href='Frames.html']").click()
sleep(5)
