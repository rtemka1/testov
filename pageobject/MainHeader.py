from lib.unit import Unit
from selene import by


class MainHeader:
    def __init__(self, unit: Unit):
        self._unit = unit

    @property
    def catalog_show_btn(self):
        return self._unit.find_elem_by_selector('.rs-catalog-show')

    @property
    def search_in_catalog_input(self):
        return self._unit.find_elem_by_selector('.form-control')

    @property
    def favourite_show_btn(self):
        return self._unit.find_elem_by_selector(by.text("Избранное"))