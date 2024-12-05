import allure
from conftest import driver
from data import Urls
from pages.main_page import MainPage


class TestHeaderLogoClick:

    @allure.title('Проверка попадания на страницу самоката после нажатия на логотип самоката')
    def test_header_logo_scooter_click(self, driver):

        main_page = MainPage(driver)
        main_page.click_to_button_order_up()
        main_page.click_to_scooter_logo()
        assert ('Самокат'
                '\nна пару дней'
                '\nПривезём его прямо к вашей двери,'
                '\nа когда накатаетесь — заберём') in main_page.get_heading_text()

    @allure.title('Проверка редиректа на страницу Дзена после нажатия на логотип Яндекса')
    #тест редиректа на страницу Дзена после нажатия на логотип Яндекса
    def test_header_logo_yandex_click(self, driver):

        main_page = MainPage(driver)
        main_page.click_to_yandex_logo()
        main_page.switch_tab_on_browser()
        main_page.wait_loading_site_dzen()
        assert main_page.get_url_dzen() == Urls.URL_DZEN_PAGE

