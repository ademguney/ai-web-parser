import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from config.settings import CHROMEDRIVER_PATH

def scrape_with_chrome(url: str, wait_time: int = 5) -> str:
    """
    Launches ChromeDriver, navigates to the given URL, and returns the raw HTML after waiting.
    """
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(executable_path=CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        print(f"[ChromeScraper] Navigating to {url} ...")
        driver.get(url)
        time.sleep(wait_time)  # Wait for the page to fully load
        return driver.page_source
    finally:
        driver.quit()