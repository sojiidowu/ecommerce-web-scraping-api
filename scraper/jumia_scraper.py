from .selenium_engine import get_driver, accept_cookies
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


logger = logging.getLogger(__name__)


def scrape_jumia_products(product_name):
    url = f'https://www.jumia.com.ng/catalog/?q={product_name}'

    logger.info("Opening Browser")

    driver = get_driver()

    try:
        logger.info('Driver created')

        driver.get(url)

        accept_cookies(driver)

        WebDriverWait(driver, 10).until(
           EC.presence_of_element_located((By.CLASS_NAME, "prd"))
        )

        products = driver.find_elements(By.CLASS_NAME, "prd")

        # Limit results to first 20 to improve performance
        products = products[:20]

        logger.info(f"Products found: {len(products)}")

        results = []

        for item in products:
            try:
                name = item.find_element(By.CLASS_NAME, "name").text
            except NoSuchElementException:
                continue

            try:
                price = item.find_element(By.CLASS_NAME, "prc").text
            except NoSuchElementException:
                price = "Unknown"

            try:
                link = item.find_element(By.CSS_SELECTOR, "a.core").get_attribute("href")
            except NoSuchElementException:
                continue

            try:
                img = item.find_element(By.CSS_SELECTOR, "div.img-c img")
                # Jumia lazy-loads images, so check data-src before src
                image = img.get_attribute("data-src") or img.get_attribute("src")
            except NoSuchElementException:
                image = "None"
                
            results.append({
                "name": name,
                "price": price,
                "link": link,
                "image": image,
            })

        logger.info("Scraping completed successfully")

        return results
    
    except Exception as e:
        logger.error(f"Scraping failed: {e}")
        return []
    
    finally:
        logger.info("Closing browser")
        driver.quit()
