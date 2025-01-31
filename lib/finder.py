from selene import Browser, by
from lib.unit import Unit
from pageobject.Checkout import Checkout
from pageobject.HeadDropdownCatalog import HeadDropdownCatalog
from pageobject.LoggedDropdown import LoggedDropdown
from pageobject.HeadBar import HeadBar
from pageobject.DropdownMenu import DropdownMenu
from pageobject.MainHeader import MainHeader
from pageobject.ModalLogin import ModalLogin
from pageobject.ModalSubmitBasket import ModalSubmitBasket
from pageobject.NotebooksInModal import NotebooksInModal
from pageobject.PhonesInModal import PhonesInModal
from pageobject.PlanshetsInModal import PlanshetsInModal
from pageobject.ProductsList import ProductsList
from pageobject.ProectorsInModal import ProectorsInModal
from pageobject.SecondDropdownCatalog import SecondDropdownCatalog
from pageobject.SelectedProductPage import SelectedProductPage
from pageobject.BasketProductPage import BasketProductPage

class Finder(Unit):
    def __init__(self, browser: Browser) -> None:
        super().__init__(browser, browser.element(''))


    @property
    def head_bar(self) -> HeadBar:
        return HeadBar(self.find_unit_by_selector('div[class="head-bar"]'))

    @property
    def dropdown_menu(self) -> DropdownMenu:
        return DropdownMenu(self.find_unit_by_selector('.head-bar__dropdown'))

    @property
    def modal_login(self) -> ModalLogin:
        return ModalLogin(self.find_unit_by_selector('.modal-content'))

    @property
    def logged_dropdown(self) -> LoggedDropdown:
        return LoggedDropdown(self.find_unit_by_selector('.lk-dropdown'))

    @property
    def head_dropdown_catalog(self) -> HeadDropdownCatalog:
        return HeadDropdownCatalog(self.find_unit_by_selector('.head-dropdown-catalog__categories'))

    @property
    def second_dropdown_catalog(self) -> SecondDropdownCatalog:
        return SecondDropdownCatalog(self.find_unit_by_selector('div[class="head-dropdown-catalog__subcat-list"]'))

    @property
    def main_header(self) -> MainHeader:
        return MainHeader(self.find_unit_by_selector('.head-main'))

    @property
    def notebooks_in_modal(self) -> NotebooksInModal:
        return NotebooksInModal(self.find_unit_by_selector('div[id="dropdown-subsubcat-2-3"]'))

    @property
    def phones_in_modal(self) -> PhonesInModal:
        return PhonesInModal(self.find_unit_by_selector('div[id="dropdown-subsubcat-2-4"]'))

    @property
    def proectors_in_modal(self) -> ProectorsInModal:
        return ProectorsInModal(self.find_unit_by_selector('div[id="dropdown-subsubcat-2-1"]'))

    @property
    def planshets_in_modal(self) -> PlanshetsInModal:
        return PlanshetsInModal(self.find_unit_by_selector('div[id="dropdown-subsubcat-2-2"]'))

    @property
    def products_list(self) -> ProductsList:
        return ProductsList(self.find_unit_by_selector('.rs-products-list'))

    @property
    def selected_product_page(self) -> SelectedProductPage:
        return SelectedProductPage(self.find_unit_by_selector('.gx-4'))

    @property
    def checkout(self) -> Checkout:
        return Checkout(self.find_unit_by_selector('.cartCheckout'))

    def basket_product_page(self, idx) -> BasketProductPage:
        return BasketProductPage(self.find_unit_by_selector(f'div[data-id="{idx}"]'))

    @property
    def modal_submit_basket(self) -> ModalSubmitBasket:
        return ModalSubmitBasket(self.find_unit_by_selector('.modal-content'))