import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


#Data driven testing with json
with open("testdata.json", 'r') as file:
    test_data = json.load(file)

# Loop through the test data and get the data
for data in test_data['users']:
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