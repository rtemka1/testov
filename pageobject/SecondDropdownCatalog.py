from lib.unit import Unit
from selene import by


class SecondDropdownCatalog:
    def __init__(self, unit: Unit):
        self._unit = unit

    @property
    def proectors(self):
        return self._unit.find_elem_by_selector(by.text('Проекторы'))

    @property
    def planshets(self):
        return self._unit.find_elem_by_selector(by.text('Планшеты'))

    @property
    def notebooks(self):
        return self._unit.find_elem_by_selector(by.text('Ноутбуки'))

    @property
    def phones(self):
        return self._unit.find_elem_by_selector(by.text('Телефоны'))

    @property
    def smartphones(self):
        return self._unit.find_elem_by_selector(by.text('Смартфоны'))

    def select_second_catalog(self, idx:str):
        return self._unit.find_elem_by_selector(by.text(idx))