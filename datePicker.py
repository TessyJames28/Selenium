from datetime import datetime, timedelta
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep



url = "https://www.globalsqa.com/demo-site/datepicker/"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

#Switching to frame to interact with the date picker
browser.find_element(By .CSS_SELECTOR, value="div[class='single_tab_div resp-tab-content resp-tab-content-active'] a[class='close_img']").click() #Close a popup instruction
frame_value = browser.find_element(By .XPATH, value="//iframe[@class='demo-frame lazyloaded']")
browser.switch_to.frame(frame_value)
sleep(5)

#Identify date picker
browser.find_element(By .CSS_SELECTOR, value="#datepicker").click()

#Handle the date picker by using the python proper date and time to get the current date
current_date = datetime.now() # Get the current date and time
next_date = current_date + timedelta(days=-7) #Use timedelta to select past or future date with '-' used for past date

formatted_date = next_date.strftime("%m/%d/%y") #Put the date in the correct format as on the website

browser.find_element(By .CSS_SELECTOR, value="#datepicker").send_keys(formatted_date + Keys.TAB) #Set the date and click tab to select
sleep(5)

browser.quit()
