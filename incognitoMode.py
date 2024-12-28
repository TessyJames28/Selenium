from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep


# Options allow us to open browser in incognito mode
chrome_options = Options()
chrome_options.add_argument("--incognito") 
# With firefox, use use --private because, the incognito mode is called private in firefox

# To open in incognitor mode, we need to pass the options to the chrome driver
url = "https://www.google.com/"
browser = webdriver.Chrome(options=chrome_options)
browser.maximize_window()
sleep(5)
browser.get(url)