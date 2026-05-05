from .selenium_engine import get_driver
import time
from selenium.webdriver.common.by import By


def scrape_jumia_products(product_name):
    url = f'https://www.jumia.com.ng/catalog/?q={product_name}'
    print("Opening Browser")
    driver = get_driver()
    print('driver created')
    driver.get(url)

    # wait for page to load
    time.sleep(5)
    # To get all product cards
    products = driver.find_elements(By.CLASS_NAME, "prd")
    print('Products found:', len(products))
    results = []

    for item in products:
        name = item.find_element(By.CLASS_NAME, "name").text
        price = item.find_element(By.CLASS_NAME, "prc").text
        link = item.find_element(By.TAG_NAME, "a").get_attribute("href")
        image = item.find_element(By.TAG_NAME, "img").get_attribute("data-src")
        

        results.append({
            "name": name,
            "price": price,
            "link": link
        })
    
    driver.quit()
    return results