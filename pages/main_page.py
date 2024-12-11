import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import Urls


class MainPage(BasePage):

    @allure.step("Получение текста ответа в разделе FAQ")
    def get_answer_text(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        self.scroll_to_element(MainPageLocators.LAST_QUESTION_LOCATOR)
        self.click_to_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step("Клик на кнопку заказа расположенную вверху страницы")
    def click_to_button_order_up(self):
        self.click_to_element(MainPageLocators.ORDER_BUTTON_UP)

    @allure.step("Клик на кнопку заказа расположенную внизу страницы")
    def click_to_button_order_down(self):
        self.click_to_element(MainPageLocators.ORDER_BUTTON_DOWN)

    @allure.step("Получение адреса ЯндексДзен")
    def get_url_dzen(self):
        return self.get_current_url()

    @allure.step("Клик на кнопку принятия куков")
    def click_cookie_accept(self):
        self.click_to_element(MainPageLocators.BUTTON_COOKIE_ACCEPT_LOCATOR)

    @allure.step("Клик на логотип самоката")
    def click_to_scooter_logo(self):
        self.click_to_element(MainPageLocators.LOGO_SCOOTER)

    @allure.step("Клик на логотип Яндекса")
    def click_to_yandex_logo(self):
        self.click_to_element(MainPageLocators.LOGO_YANDEX)

    @allure.step("Получение текста заголовка")
    def get_heading_text(self):
        return self.get_text_from_element(MainPageLocators.HEADING_TEXT)

    @allure.step("Переключение вкладки браузера")
    def switch_tab_on_browser(self):
        return self.switch_tab()

    @allure.step("Ожидание загрузки страницы Дзена")
    def wait_loading_site_dzen(self):
        self.wait_loading_site(Urls.URL_DZEN_PAGE)

    @allure.step("Получение адреса Дзена")
    def get_url_dzen(self):
        return self.get_current_url()