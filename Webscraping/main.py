from selenium import webdriver
from time import sleep


# Webscraping Amazon website
browser = webdriver.Chrome()
url = "https://www.amazon.com/?tag=hymsabk-20&ref=pd_sl_6gwjrxu9p1_e&adgrpid=1341405838299434&hvadid=83838130693495&hvnetw=o&hvqmt=e&hvbmt=be&hvdev=c&hvlocint=&hvlocphy=152654&hvtargid=kwd-83838874655187:loc-137&hydadcr=28884_14559613&msclkid=1cac9204bdbf1b569185f5760064835c"
browser.get(url)
sleep(3)
