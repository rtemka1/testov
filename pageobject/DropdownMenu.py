from lib.unit import Unit
from selene import by


class DropdownMenu:
    def __init__(self, unit: Unit):
        self._unit = unit

    @property
    def login_btn(self):
        return self._unit.find_elem_by_selector('a[href="/auth/?referer=%252F"]')

    @property
    def register_btn(self):
        return self._unit.find_elem_by_selector('a[href="/register/?referer=%252F"]')