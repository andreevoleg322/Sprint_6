import pytest
from selenium import webdriver
from data import Urls


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.URL_MAIN_PAGE)
    yield driver
    driver.quit()
