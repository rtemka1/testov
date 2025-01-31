import dotenv
import pytest
from selene.core.configuration import Config
from lib.driver import Driver
from selene import be

@pytest.fixture(scope='function')
def envs():
    dotenv.load_dotenv()

@pytest.fixture(scope='function')
def driver(envs):
    base_url = "https://mega.readyscript.ru/"
    if not base_url:
        raise Exception("CLIENT_BASE_URL is not defined in environment variables.")
    driver_instance = Driver(base_url=base_url)
    yield driver_instance
    driver_instance.close()

@pytest.fixture(scope='function')
def login(driver):
    driver.open()
    driver.head_bar.lk_btn.should(be.visible).click()
    driver.dropdown_menu.login_btn.should(be.visible).click()
    driver.modal_login.login_input.click().clear()
    driver.modal_login.login_input.type("qwerty@example.com")
    driver.modal_login.pass_input.click().clear()
    driver.modal_login.pass_input.type("qwe12345678")
    driver.modal_login.submit_btn.should(be.visible).click()