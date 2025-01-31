from selene import be, query


def test_check_login(driver, login):
    login = "Артем Артемов"
    driver.head_bar.lk_btn.should(be.visible).click()
    assert driver.logged_dropdown.fetch_info.get(query.text) == login