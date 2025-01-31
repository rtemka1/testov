from selene import be, query


def test_check_login(driver, login):
    login = "Артем Артемов"
    driver.main_header.lk_btn.should(be.visible).click()
    assert driver.logged_dropdown.fetch_info.get(query.text) == login