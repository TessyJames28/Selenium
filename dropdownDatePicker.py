from datetime import datetime, timedelta
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep



url = "https://demo.automationtesting.in/Datepicker.html"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

#Click on the date picker field
browser.find_element(By .ID, value="datepicker2").click()
sleep(3)

# Grab the date using timedelta
current_date = datetime.now()
print(current_date)

next_day = current_date + timedelta(days=1)
print(next_day)
#Converting to string so we can pass as value
next_new_day = (str(next_day.day)) # day
print(next_new_day)
current_month = datetime.now().month
current_year = current_date.year

next_month = (current_month % 12) + 1
next_month_year = f"{next_month}/{current_year}" # Got the value based on the date picker inspect element

# Handle the drop down for month
month_dropdown = browser.find_element(By .CSS_SELECTOR, value="select[title='Change the month']")
select = Select(month_dropdown) # Select the dropdown month
select.select_by_value(str(next_month_year))

# Handle the drop down for year
year_dropdown = browser.find_element(By .CSS_SELECTOR, value="select[title='Change the year']")
select = Select(year_dropdown)
select.select_by_visible_text("2025")

# Handle the date 
browser.find_element(By .LINK_TEXT, next_new_day).click()
sleep(5)