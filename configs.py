import os
from selene import Browser, Config
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options


def build_browser(base_url, mobile_view: bool = False, run_on_external_browser: bool = False) -> Browser:
    is_user_external_selenoid = run_on_external_browser or os.getenv("ENV_CI_CD") == '1'

    browser.config.base_url = base_url
    if mobile_view:
        browser.config.mobile = True
        browser.config.window_width = 375
        browser.config.window_height = 667
    else:
        browser.config.mobile = False
        browser.config.window_width = 1440
        browser.config.window_height = 1200

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--font-render-hinting=none")
    chrome_options.add_experimental_option('detach', True)

    if is_user_external_selenoid:
        capabilities = {
            "browserName": "chrome",
            "browserVersion": "latest",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False,
                "timeZone": "Europe/Moscow",
            }
        }

        for key, value in capabilities.items():
            chrome_options.set_capability(key, value)

        browser.config.driver = webdriver.Remote(
            command_executor=os.getenv("SELENIUM_REMOTE_URL", 'http://selenium:4444/wd/hub'),
            options=chrome_options
        )
    else:
        browser.config.driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)

    return Browser(Config(base_url=base_url))
