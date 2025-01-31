from lib.unit import Unit
from selene import by


class PlanshetsInModal:
    def __init__(self, unit: Unit):
        self._unit = unit


    @property
    def archos(self):
        return self._unit.find_elem_by_selector(by.text('Archos'))


    @property
    def digma(self):
        return self._unit.find_elem_by_selector(by.text('Digma'))


    @property
    def htc(self):
        return self._unit.find_elem_by_selector(by.text('HTC'))


    @property
    def creative(self):
        return self._unit.find_elem_by_selector(by.text('Creative'))

    @property
    def viewsonic(self):
        return self._unit.find_elem_by_selector(by.text('ViewSonic'))
