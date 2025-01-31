from selene import be
import time

def test_add_basket(driver, login):
    #id нашего продукта
    my_idx="31"
    #производитель ноутов
    notebook_producer = "MSI"
    driver.main_header.catalog_show_btn.should(be.visible).click()
    driver.head_dropdown_catalog.electronics.should(be.visible).hover()
    driver.second_dropdown_catalog.notebooks.should(be.visible).hover()
    driver.notebooks_in_modal.select_notebook(notebook_producer).should(be.visible).click()
    driver.products_list.select_item(my_idx).should(be.visible).click()
    driver.selected_product_page.add_to_basket(my_idx).should(be.visible).click()
    driver.modal_submit_basket.go_to_basket.should(be.visible).click()
    driver.basket_product_page(my_idx).delete_product.should(be.visible).click()