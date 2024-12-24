from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import requests

url = "https://jqueryui.com/"
browser = webdriver.Chrome()
browser.get(url)
browser.maximize_window()

# Getting all broken link by getting all anchor tags
all_links = browser.find_elements(By .TAG_NAME, value="a")
print(f"Total number of links on the page is {len(all_links)}")
broken_links = []

# Check for broken links
for link in all_links:
    href = link.get_attribute('href')
    if not href:
        print(f"Not a valid link: {href}")
    # Use the request library to access the link
    try:
        response = requests.get(href, timeout=5)
        if response.status_code >= 400:
            print(f"Broken Link: {href}\t(status_code: {response.status_code})")
    except requests.exceptions.MissingSchema:
        pass
    except requests.exceptions.RequestException as e:
        pass



browser.quit()
