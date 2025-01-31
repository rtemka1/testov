from lib.unit import Unit
from selene import by


class Checkout:
    def __init__(self, unit: Unit):
        self._unit = unit

    @property
    def clear_basket(self):
        return self._unit.find_elem_by_selector('.cart-checkout-clear rs-clean')