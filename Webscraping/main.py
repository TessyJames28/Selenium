from PIL import Image, ImageOps
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytesseract


# Point pytesseract to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Webscraping Amazon website
browser = webdriver.Chrome()
browser.maximize_window()
# browser.implicitly_wait(20)
url = "https://www.amazon.com/?tag=hymsabk-20&ref=pd_sl_6gwjrxu9p1_e&adgrpid=1341405838299434&hvadid=83838130693495&hvnetw=o&hvqmt=e&hvbmt=be&hvdev=c&hvlocint=&hvlocphy=152654&hvtargid=kwd-83838874655187:loc-137&hydadcr=28884_14559613&msclkid=1cac9204bdbf1b569185f5760064835c"
browser.get(url)

captcha_element = browser.find_element(By .TAG_NAME, value="img")
captcha_element.screenshot("captcha.png")

# Processing image
image = Image.open("captcha.png")
image = ImageOps.grayscale(image)
image = image.point(lambda p: p > 128 and 255)
image.save("prepocessed_captcha.png")

captcha_text = pytesseract.image_to_string(image)
print(f"Extracted CAPTCHA Text: {captcha_text}")
