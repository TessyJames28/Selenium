from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url = "https://cosmocode.io/automation-practice-webtable/"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

# Execute script to scroll down the page to access the table
browser.execute_script("window.scrollTo(0, 700)")
sleep(2)

# Identify the target table
table = browser.find_element(By .ID, value="countries") # find element by entire table ID
rows = table.find_elements(By .TAG_NAME, value="tr") # Get all the rows in the table
row_count = len(rows)
print(f"Row count: {row_count}")
target_value = "Australias"
found = False

# Loop through the row to find the target value
for row in rows:
    cells = row.find_elements(By .TAG_NAME, value="td") # Find the cells and loop through the,
    for cell in cells:
        if target_value in cell.text: #Get cell with the desired value
            found = True
            print(f"Target value found: {found}\nTarget value: {cell.text}")
    if found:
        break
if not found:
    print(f"Target value found: {found}")