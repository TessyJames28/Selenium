from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import requests

url = "https://the-internet.herokuapp.com/broken_images"
browser = webdriver.Chrome()
browser.get(url)
browser.maximize_window()
sleep(5)
browser.minimize_window()

images = browser.find_elements(By .TAG_NAME, value="img")
broken_images = []

# Loop through the images to find broken image
for image in images:
    src = image.get_attribute("src")
    if src:
        response = requests.get(src)
        if response.status_code != 200:
            broken_images.append(src)
            print(f"Broken image found")


# Loop through the list of broken images
if broken_images:
    print(f"===== List of broken images=====")
    for image in broken_images:
        print(image)