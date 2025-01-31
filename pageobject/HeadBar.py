from lib.unit import Unit
from selene import by


class HeadBar:
    def __init__(self, unit: Unit):
        self._unit = unit

    @property
    def lk_btn(self):
        return self._unit.find_elem_by_selector('a[data-bs-toggle="dropdown"]')

    @property
    def other_town(self):
        return self._unit.find_elem_by_selector('Другой город')

    @property
    def home_page(self):
        return self._unit.find_elem_by_selector('главная')

    @property
    def pay(self):
        return self._unit.find_elem_by_selector('главная')

    @property
    def delivery(self):
        return self._unit.find_elem_by_selector('главная')

    @property
    def contacts(self):
        return self._unit.find_elem_by_selector('главная')