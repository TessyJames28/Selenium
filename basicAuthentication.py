from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep


url = ""
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)