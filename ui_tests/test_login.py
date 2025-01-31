from selene import be
import time

def test_login(driver):
    driver.open()
    driver.head_bar.lk_btn.should(be.visible).click()
    driver.dropdown_menu.login_btn.should(be.visible).click()
    driver.modal_login.login_input.click().clear()
    driver.modal_login.login_input.type("qwerty@example.com")
    driver.modal_login.pass_input.click().clear()
    driver.modal_login.pass_input.type("qwe12345678")
    driver.modal_login.submit_btn.should(be.visible).click()