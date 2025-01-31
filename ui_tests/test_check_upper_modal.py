from selene import be

def test_check_upper_modal(driver,login):
    driver.main_header.catalog_show_btn.should(be.visible).click()
    driver.head_dropdown_catalog.electronics.should(be.visible).hover()
    driver.second_dropdown_catalog.planshets.should(be.visible).hover()
    driver.planshets_in_modal.digma.should(be.visible)
