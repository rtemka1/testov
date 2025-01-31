from lib.unit import Unit
from selene import by


class FavouritePage:
    def __init__(self, unit: Unit):
        self._unit = unit

    def select_favor_item(self, idx):
        return self._unit.find_elem_by_selector(f'div[data-id="{idx}"]')