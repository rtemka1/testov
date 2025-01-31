from lib.unit import Unit
from selene import by


class ModalAutocomplete:
    def __init__(self, unit: Unit):
        self._unit = unit

    def select_result(self, idx):
        return self._unit.find_elem_by_selector(by.partial_text(idx))