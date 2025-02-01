from selene import Browser, Config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options


def build_browser(base_url) -> Browser:
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--font-render-hinting=none")

    driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)

    return Browser(Config(base_url=base_url, driver=driver))