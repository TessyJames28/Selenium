from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Trying out different browser commands
browser = webdriver.Chrome()
browser.get("https://fs2.formsite.com/meherpavan/form2/index.html")
browser.maximize_window()

# To execute script: The script will scroll to available height
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
sleep(1)


# To grab all the checkboxex, this time they will unclick
checkboxes = browser.find_elements(By .XPATH, value="//input[@type='checkbox']")
for checkbox in checkboxes:
    checkbox.send_keys(Keys.SPACE) # You can use .click() as well as Keys.SPACE, using the space tab to check
    sleep(1)


# Refetching the elements for proper interactions
checkboxes = browser.find_elements(By .XPATH, value="//input[@type='checkbox']")

checkbox_count = 0
expected_count = 7
for check in checkboxes:
    if check.is_selected():
        checkbox_count += 1
        sleep(1)

if expected_count == checkbox_count:
    print("Checkboxes verified")
else:  
    print("Checkboxes not verified")