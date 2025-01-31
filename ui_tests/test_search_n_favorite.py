import pytest
from selene import be, query

class TestSearchNFavorite:


    idx=93
    @pytest.fixture(autouse=True)
    def favor_post_condition(self, driver, login):
        yield
        idx = 93
        driver.main_header.favourite_show_btn.click()
        driver.selected_favor_item(idx=idx).in_favority.click()

    def test_search_n_favorite(self, driver, login):
        idx = 93
        driver.main_header.search_in_catalog_input.click().type("Alcatel")
        driver.modal_autocomplete.select_result('OneTouch 806 Bronze').should(be.visible).click()
        driver.selected_product_page.add_to_favourite.should(be.visible).click()
        driver.main_header.favourite_show_btn.should(be.visible).click()
        driver.favourite_page.select_favor_item(idx=idx).should(be.visible)
        assert driver.selected_favor_item(idx=idx).item_title.get(query.text) == "Alcatel OneTouch 806 Bronze"
