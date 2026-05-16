from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from  selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--start-maximized")

    chrome_options.add_argument(
        "--disable-blink-features=AutomationControlled")

    chrome_options.add_argument("--disable-infobars")

    chrome_options.add_argument("--disable-extensions")

    chrome_options.add_argument("--no-sandbox")

    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)

    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    )

    return driver

def accept_cookies(driver):
    try:
        WebDriverWait(driver, 5).until(
             EC.element_to_be_clickable(
                 (By.XPATH,"//button[contains(text(), 'Accept') or contains(text(), 'accept')]")
             )
        ).click()
    except:
        pass