from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url = "https://the-internet.herokuapp.com/iframe"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

#Based on the example website, get the text editor
# First find the iframe and switch to it
iframe = browser.find_element(By .ID, value="mce_0_ifr")
browser.switch_to.frame(iframe) # Switch to the iframe

text_editor = browser.find_element(By .ID, value="tinymce")
#Execute script to change contenteditable from false to true for testing
browser.execute_script("arguments[0].setAttribute('contenteditable', 'true');", text_editor)
text_editor.clear() # clear the text editor of default text
text_editor.send_keys("This is a practise round on web automation handling iframes")
sleep(5)

# Access content outside the iframe
browser.switch_to.default_content() # switch back to the main content, i.e, the main html content
selenium_link = browser.find_element(By .XPATH, value="//a[normalize-space()='Elemental Selenium']")
selenium_link.click()
sleep(5)