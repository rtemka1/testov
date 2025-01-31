from lib.unit import Unit
from selene import by


class SelectedProductPage:
    def __init__(self, unit: Unit):
        self._unit = unit


    def add_to_basket(self,idx):
        return self._unit.find_elem_by_selector(f'button[data-href="/cart/?add={idx}"]')