from lib.unit import Unit
from selene import by


class ProectorsInModal:
    def __init__(self, unit: Unit):
        self._unit = unit


    @property
    def optoma(self):
        return self._unit.find_elem_by_selector(by.text('Optoma'))


    @property
    def samsung(self):
        return self._unit.find_elem_by_selector(by.text('Samsung'))


    @property
    def sanyo(self):
        return self._unit.find_elem_by_selector(by.text('Sanyo'))


    @property
    def viewsonic(self):
        return self._unit.find_elem_by_selector(by.text('ViewSonic'))


    @property
    def nec(self):
        return self._unit.find_elem_by_selector(by.text('Nec'))


    @property
    def sony(self):
        return self._unit.find_elem_by_selector(by.text('Sony'))


    @property
    def panasonic(self):
        return self._unit.find_elem_by_selector(by.text('Panasonic'))


    @property
    def canon(self):
        return self._unit.find_elem_by_selector(by.text('Canon'))