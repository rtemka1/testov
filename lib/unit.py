import re
from selene import Browser, have, be
from selene.core.entity import Element


def find_all_units(s: str):
    return re.findall(r'data-unit-id=[\'"]?([^\'">]+)', s)


class Unit:
    def __init__(self, browser: Browser, element: Element) -> None:
        self._browser = browser
        self._el = element

    def find_elem(self, el_id: str) -> Element:
        return self._el.element(f'[data-id="{el_id}"]')

    def find_unit(self, unit_id: str, entity_id: str = None, object_id: str = None,
                  assert_visible: bool = True) -> 'Unit':
        """
        Поиск юнита по заданным идентификаторам.
        """
        unit_selector = self._build_unit_selector(unit_id, entity_id, object_id)
        unit = Unit(self._browser, self._browser.element(unit_selector))
        if assert_visible:
            unit._el.should(be.visible)
        return unit

    def find_unit_by_selector(self, unit_selector: str, assert_visible: bool = True) -> 'Unit':
        """
        Поиск юнита по пользовательскому селектору.
        """
        unit = Unit(self._browser, self._browser.element(unit_selector))
        if assert_visible:
            unit._el.should(be.visible)
        return unit

    def find_elem_by_selector(self, selector: str) -> Element:
        return self._el.element(selector)

    def find_unit_list(self, unit_id: str, entity_id: str = None, object_id: str = None):
        """
        Поиск всех юнитов по заданным идентификаторам.
        """
        selector = self._build_unit_selector(unit_id, entity_id, object_id)
        elements = self._browser.all(selector)
        for el in elements:
            yield Unit(self._browser, el)

    def _build_unit_selector(self, unit_id: str, entity_id: str = None, object_id: str = None) -> str:
        """
        Построение селектора на основе переданных идентификаторов.
        """
        selector = f'[data-test-id="{unit_id}"]'
        if entity_id:
            selector += f'[data-entity-id="{entity_id}"]'
        if object_id:
            selector += f'[data-object-id="{object_id}"]'
        return selector
