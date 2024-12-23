from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Trying out device responsiveness
viewports = [(1024, 768), (768, 1024), (375, 667), (414, 896)]
browser = webdriver.Chrome()
browser.get("https://google.com/")


try:
    for width, height in viewports:
        browser.set_window_size(width, height)
        sleep(5)

finally:
    browser.close()