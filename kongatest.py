from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    TimeoutException,
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


driver = webdriver.Chrome()
driver.maximize_window()
# Category navigation for konga
def navigate_konga_categories(driver):
    actions = ActionChains(driver)
    driver.get("https://www.konga.com/")

    # Navigate to category, hover and click on electronics
    category = driver.find_element(By .XPATH, value = "//a[normalize-space()='All Categories']")
    actions.move_to_element(category).perform()
    sleep(3)
    driver.find_element(By .XPATH, value = "//body//div//div//section//div//div//div//div//div//ul//li//a[contains(text(),'Electronics')]").click()
    sleep(5)

    scrape_konga_pages(driver)


def next_page(driver, path_value):
    page_num = driver.find_element(By .CSS_SELECTOR, "._7f300_PqGPC").text
    total_pages = driver.find_element(By .XPATH, "//a[normalize-space()='25']").text
    print(f"Total pages: {total_pages}\tPage num: {page_num}")
    if page_num == total_pages:
            print("No more pages")
            return False
    try:
        # Navigate to the next button on webpage
        next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By .XPATH, path_value)
        ))

        # Scroll into view of the next button and click it
        driver.execute_script("arguments[0].scrollIntoView();", next_button)
        driver.execute_script("arguments[0].click();", next_button)
        sleep(5) # Waits for the page to load

        return True
        # if page_num == total_pages:
        #     print("No more pages")
        #     return False

    except TimeoutException:
        print("No more pages")
        return False



# Scrape Konga website
def scrape_konga_pages(driver):
    while True:
        soup = BeautifulSoup(driver.page_source, "lxml")
        product_container = soup.find("ul", attrs={"class": "b49ee_2pjyI _58c31_2R34y _22339_3gQb9"})
        products = product_container.find_all("li")

        # Confirm the selection of the product container
        if products:
            for product in products:
                # Get the title
                title = (
                    product.find("h3", class_ = "af885_1iPzH").get_text(strip = True)
                    if product.find("h3", class_ = "af885_1iPzH")
                    else None
                )

                # Get the image url
                image_tag = product.find("img")
                image_url = (
                    image_tag["src"]
                    if image_tag and "src" in image_tag.attrs
                    else None
                )

                # Get the product url
                product_url = (
                    "https://www.konga.com/" + product.find("a")["href"]
                    if product.find("a")["href"]
                    else None
                )

                # Get product price
                product_price = (
                    product.find("span", class_ = "d7c0f_sJAqi").get_text(strip = True)
                    if product.find("span", class_ = "d7c0f_sJAqi")
                    else None
                )

                # Extract the category dynamically (This depends on the website structure)
                category = (
                    soup.find("h1", class_ = "_9590c_10MV8").get_text(strip = True)
                    if soup.find("h1", class_ = "_9590c_10MV8")
                    else None
                )
                print(f"""
    title: {title}\n
    image_url: {image_url}\n
    product_url: {product_url}\n
    product_price: {product_price}\n
    category: {category}\n
    """)
        if not next_page(driver, "//a[normalize-space()='Next']"):
            break


navigate_konga_categories(driver)