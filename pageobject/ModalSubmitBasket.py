from lib.unit import Unit
from selene import by


class ModalSubmitBasket:
    def __init__(self, unit: Unit):
        self._unit = unit

    @property
    def go_to_basket(self):
        return self._unit.find_elem_by_selector(by.text('Перейти в корзину'))