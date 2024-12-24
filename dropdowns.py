from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome()
browser.maximize_window()
login_url = "https://the-internet.herokuapp.com/dropdown"
browser.get(login_url)

# To interact with the dropdown menu, we need to interact with the select element
dropdown_element = browser.find_element(By .ID, value="dropdown") #dropdown element
select = Select(dropdown_element) 
sleep(3)

# Select value by visible text
# Select the alue by index
# Select the option by using a value

# select.select_by_visible_text("Option 2")
# select.select_by_index(1) 
# select.select_by_value("2")

# Testing the option count: Note that the subheading on the option is part of the index
# option_count = len(select.options)
# expected_count = 3
# if option_count == expected_count:
#     print("Test case passed: count is correct")
# else:
#     print("Test case failed: count is incorrect")

# Selecting option by targeting a particular value
target_value = "Option 2"

for option in select.options:
    if option.text == target_value:
        option.click()
        sleep(3)
        print(f"The target option {target_value} is selected")
        break
    else:
        print(f"The target option '{target_value}' is not found.")
