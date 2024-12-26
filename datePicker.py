from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


url = "https://www.globalsqa.com/demo-site/datepicker/"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

#Switching to frame to interact with the date picker
browser.find_element(By .XPATH, value="//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//div[@class='attention closable'][normalize-space()='Pick a date by clicking on the text box.']").click()
frame_value = browser.find_element(By .XPATH, value="//iframe[@class='demo-frame lazyloaded']")
