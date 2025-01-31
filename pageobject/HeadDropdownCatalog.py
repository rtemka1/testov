from lib.unit import Unit
from selene import by


class HeadDropdownCatalog:
    def __init__(self, unit: Unit):
        self._unit = unit

    @property
    def demo_products(self):
        return self._unit.find_elem_by_selector(by.text('Демо-продукты'))

    @property
    def electronics(self):
        return self._unit.find_elem_by_selector(by.text('Электроника'))

    @property
    def cloth_and_shoes(self):
        return self._unit.find_elem_by_selector(by.text('Одежда, обувь'))

    @property
    def kid_stuff(self):
        return self._unit.find_elem_by_selector(by.text('Детские товары'))

    @property
    def sport(self):
        return self._unit.find_unit_by_selector(by.text('Спорт товары'))

    @property
    def gifts(self):
        return self._unit.find_elem_by_selector(by.text('Подарки'))