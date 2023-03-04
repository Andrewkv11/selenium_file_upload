import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver = webdriver.Remote(
    #     command_executor='http://localhost:4444/wd/hub',
    #     options=webdriver.ChromeOptions())
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def open_login_page(driver):
    login_page = LoginPage(driver)
    driver.get('http://localhost:80/sign-in')
    return login_page


@pytest.fixture()
def authorization(open_login_page):
    open_login_page.fill_authorization_form()
    open_login_page.submit_authorization()
    return open_login_page
