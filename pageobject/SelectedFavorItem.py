from lib.unit import Unit
from selene import by


class SelectedFavorItem:
    def __init__(self, unit: Unit):
        self._unit = unit

    @property
    def item_title(self):
        return self._unit.find_elem_by_selector('.item-card__title')

    @property
    def in_favority(self):
        return self._unit.find_elem_by_selector('.rs-in-favorite')