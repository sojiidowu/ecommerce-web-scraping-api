from .selenium_engine import get_driver, accept_cookies
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def scrape_jumia_products(product_name):
    url = f'https://www.jumia.com.ng/catalog/?q={product_name}'
    print("Opening Browser")
    driver = get_driver()
    print('driver created')
    driver.get(url)

    accept_cookies(driver)

    # wait for page to load
    time.sleep(5)
    # To get all product cards
    products = driver.find_elements(By.CLASS_NAME, "prd")
    products = products[:20]
    print('Products found:', len(products))
    results = []

    for item in products:
        # Product Name
        try:
            name = item.find_element(By.CLASS_NAME, "name").text
        except NoSuchElementException:
            continue
        # Product Price
        try:
            price = item.find_element(By.CLASS_NAME, "prc").text
        except NoSuchElementException:
            price = "Unknown"
        # Product Link
        try:
            link = item.find_element(By.CSS_SELECTOR, "a.core").get_attribute("href")
        except NoSuchElementException:
            continue
        # Product Image
        try:
            img = item.find_element(By.CSS_SELECTOR, "div.img-c img")
            image = img.get_attribute("data-src") or img.get_attribute("src")
        except NoSuchElementException:
            image = "None"

        # Storing scraped data in a dictionary
        results.append({
            "name": name,
            "price": price,
            "link": link,
            "image": image,
        })
    driver.quit()
    
    return results