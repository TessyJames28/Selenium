from selenium import webdriver
from selenium.webdriver.common.by import By


url = "https://the-internet.herokuapp.com/nested_frames"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

# The test website has the top and bottom frame which are inside a frameset
# Switching to top frame
browser.switch_to.frame("frame-top")

# Switching to middle frame to get the content
browser.switch_to.frame("frame-middle")
content = browser.find_element(By .ID, value="content").text
print(f"Content in Middle frame is: {content}")

# Leave the frame by switching to default content
browser.switch_to.default_content()

# Switch to bottom frame
browser.switch_to.frame("frame-bottom")
content_bottom = browser.find_element(By .TAG_NAME, value="body").text
print(f"Content in Bottom frame is: {content_bottom}")
