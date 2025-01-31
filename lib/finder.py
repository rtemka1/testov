from selene import Browser, by
from lib.unit import Unit
from pageobject.LoggedDropdown import LoggedDropdown
from pageobject.MainHeader import MainHeader
from pageobject.DropdownMenu import DropdownMenu
from pageobject.ModalLogin import ModalLogin


class Finder(Unit):
    def __init__(self, browser: Browser) -> None:
        super().__init__(browser, browser.element(''))


    @property
    def main_header(self) -> MainHeader:
        return MainHeader(self.find_unit_by_selector('div[class="head-bar"]'))

    @property
    def dropdown_menu(self) -> DropdownMenu:
        return DropdownMenu(self.find_unit_by_selector('.head-bar__dropdown'))

    @property
    def modal_login(self) -> ModalLogin:
        return ModalLogin(self.find_unit_by_selector('.modal-content'))

    @property
    def logged_dropdown(self) -> LoggedDropdown:
        return LoggedDropdown(self.find_unit_by_selector('.lk-dropdown'))
