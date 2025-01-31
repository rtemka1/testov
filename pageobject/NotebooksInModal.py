from lib.unit import Unit
from selene import by


class NotebooksInModal:
    def __init__(self, unit: Unit):
        self._unit = unit


    def select_notebook(self, idx:str):
        return self._unit.find_elem_by_selector(by.text(idx))