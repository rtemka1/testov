from lib.unit import Unit
from selene import by


class BasketProductPage:
    def __init__(self, unit: Unit):
        self._unit = unit

    @property
    def delete_product(self):
        return self._unit.find_elem_by_selector('.rs-remove')