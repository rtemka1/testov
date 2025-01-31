import os

from selene import Browser, Config
from selene.support.shared import browser
from selenium import webdriver

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

    if is_user_external_selenoid:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_experimental_option('detach', True)
        chrome_options.add_argument("--font-render-hinting=none")

        capabilities = {
            "browserName": "chrome",
            "browserVersion": "latest",
            "loggingPrefs": {'browser': 'ALL'},
            "seleniumOptions": {
                "enableVNC": True,
                "enableVideo": False,
                "timeZone": "Europe/Moscow",
            }
        }

        for key, value in capabilities.items():
            chrome_options.set_capability(key, value)

        browser.config.driver = webdriver.Remote(
            command_executor='http://selenium:4444/wd/hub',
            options=chrome_options
        )
    return Browser(Config(base_url=base_url))

