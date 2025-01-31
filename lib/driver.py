import logging
from selene import command
from selene import Element
from configs import build_browser
from lib.finder import Finder


class Driver(Finder):
    def __init__(self, base_url: str):
        if not base_url:
            raise ValueError("Base URL cannot be None or empty.")
        self._base_url = base_url
        self._browser = build_browser(base_url=base_url)

    def open(self, url: str = ""):
        full_url = f"{self._base_url}{url}"
        logging.info(f'Opening {full_url}')
        self._browser.driver.maximize_window()
        self._browser.open(full_url)

    def close(self):
        try:
            self._browser.driver.quit()
        except Exception as e:
            logging.error(f"Ошибка при закрытии браузера: {e}")

    def __open_only(self, url: str):
        logging.info(f"Opening {url}")
        self._browser.open(url)

    def remove_element_from_dom(self, el: Element):
        el.perform(command.js.remove)

    def switch_window(self):
        return self._browser.driver.switch_to.window(self._browser.driver.window_handles[1])

    def check_current_url(self, param: str):
        url = self._browser.driver.current_url
        assert url == param, f"{url} != {param}"

    def refresh_page(self):
        self._browser.driver.refresh()
