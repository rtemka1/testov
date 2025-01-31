from selene import be, query


def test_check_login(driver, login):
    driver.main_header.lk_btn.should(be.visible).click()
    penes = driver.logged_dropdown.fetch_info.get(query.text)
    

    assert penes == "Артем Артемов"