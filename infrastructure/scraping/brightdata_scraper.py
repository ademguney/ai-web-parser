from config.settings import SBR_WEBDRIVER
from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection

def scrape_with_brightdata(url: str, detect_timeout: int = 10000) -> str:
    """
    Uses Bright Data Scraping Browser to load the page and return raw HTML.
    Automatically waits for CAPTCHA to be solved.
    """
    print("[BrightDataScraper] Connecting to Bright Data Scraping Browser...")

    connection = ChromiumRemoteConnection(SBR_WEBDRIVER, "goog", "chrome")

    options = ChromeOptions()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    with Remote(command_executor=connection, options=options) as driver:
        driver.get(url)
        print("[BrightDataScraper] Waiting for CAPTCHA solve...")

        solve_res = driver.execute(
            "executeCdpCommand",
            {
                "cmd": "Captcha.waitForSolve",
                "params": {"detectTimeout": detect_timeout},
            },
        )

        print("Captcha solve status:", solve_res["value"]["status"])
        html = driver.page_source
        return html
