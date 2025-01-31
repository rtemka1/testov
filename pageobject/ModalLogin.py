from lib.unit import Unit
from selene import by


class ModalLogin:
    def __init__(self, unit: Unit):
        self._unit = unit

    @property
    def login_input(self):
        return self._unit.find_elem_by_selector('input[name="login"]')

    @property
    def pass_input(self):
        return self._unit.find_elem_by_selector('input[name="pass"]')

    @property
    def submit_btn(self):
        return self._unit.find_elem_by_selector('button[type="submit"]')