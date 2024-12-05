from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import Urls


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    #получение текста ответа в разделе FAQ
    def get_answer_text(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        self.scroll_to_element(MainPageLocators.LAST_QUESTION_LOCATOR)
        self.click_to_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)

    #клик на кнопку заказа расположенную вверху страницы
    def click_to_button_order_up(self):
        self.click_to_element(MainPageLocators.ORDER_BUTTON_UP)

    #клик на кнопку заказа расположенную внизу страницы
    def click_to_button_order_down(self):
        self.click_to_element(MainPageLocators.ORDER_BUTTON_DOWN)

    #получение адреса ЯндексДзен
    def get_url_dzen(self):
        return self.get_current_url()

    #получение текста в всплывающем окне успешного заказа
    def check_order(self, locator):
        return self.get_text_from_element(locator)

    #клик на кнопку "заказать"
    def click_to_order_button(self, locator):
        self.click_to_element(locator)

    #клик на принятие куков
    def click_cookie_accept(self, locator):
        self.click_to_element(locator)

    #клик в пустое место на странице
    def click_to_empty_place_on_page(self, locator):
        self.click_to_element(locator)

    #клик на логотип самоката
    def click_to_scooter_logo(self):
        self.click_to_element(MainPageLocators.LOGO_SCOOTER)

    #клик на логотип Яндекса
    def click_to_yandex_logo(self):
        self.click_to_element(MainPageLocators.LOGO_YANDEX)

    #получение текста заголовка
    def get_heading_text(self):
        return self.get_text_from_element(MainPageLocators.HEADING_TEXT)

    #переключение закладки браузера
    def switch_tab_on_browser(self):
        return self.switch_tab()

    #ожидание загрузки страницы Дзена
    def wait_loading_site_dzen(self):
        self.wait_loading_site(Urls.URL_DZEN_PAGE)

    #получение адреса Дзена
    def get_url_dzen(self):
        return self.get_current_url()