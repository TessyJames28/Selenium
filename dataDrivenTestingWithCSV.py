import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


# Load the csv file
csv_file = "testdata.csv"
test_data = []

# Read the csv file
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)

    # Loop through the reader
    for row in reader:
        test_data.append(row)
print(test_data)

# Loop through the test data and get the data
for data in test_data:
    print(f"{data['username']}: {'password'}")
    url = "https://www.saucedemo.com/"
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(url)
    sleep(5)

    browser.find_element(By .ID, value="user-name").send_keys(data['username'])
    browser.find_element(By .ID, value="password").send_keys(data['password'])

    browser.find_element(By .ID, value="login-button").click()
    sleep(5)