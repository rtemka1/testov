from lib.unit import Unit
from selene import by


class LoggedDropdown:
    def __init__(self, unit: Unit):
        self._unit = unit

    @property
    def dropdown_head(self):
        return self._unit.find_elem_by_selector('.lk-dropdown__head')

    @property
    def my_profile(self):
        return self._unit.find_elem_by_selector(by.text('Мой профиль'))

    @property
    def my_orders(self):
        return self._unit.find_elem_by_selector(by.text('Мои заказы'))

    @property
    def my_backs(self):
        return self._unit.find_elem_by_selector(by.text('Мои возвраты'))

    @property
    def my_check(self):
        return self._unit.find_elem_by_selector(by.text('Лицевой счет'))

    @property
    def my_msgs(self):
        return self._unit.find_elem_by_selector(by.partial_text('Сообщения'))

    @property
    def logout(self):
        return self._unit.find_elem_by_selector('.lk-logout')

    @property
    def fetch_info(self):
        return self._unit.find_elem_by_selector('.fw-bold')