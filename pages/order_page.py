import allure
import data
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

class OrderPage(BasePage):

    @allure.step("Заполнение 1 страницы формы заказа")
    def set_order_form_1(self):
        self.add_text_to_element(OrderPageLocators.FIRST_NAME_INPUT, data.OrderData.first_name)
        self.add_text_to_element(OrderPageLocators.LAST_NAME_INPUT, data.OrderData.last_name)
        self.add_text_to_element(OrderPageLocators.ADDRESS_INPUT, data.OrderData.address)
        self.click_to_element(OrderPageLocators.METRO_STATION_INPUT)
        self.click_to_element(OrderPageLocators.FIRST_STATION_CHOSE)
        self.add_text_to_element(OrderPageLocators.PHONE_INPUT, data.OrderData.phone)
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнение второй страницы формы заказа")
    def set_order_form_2(self, locator_rent_day):
        self.add_text_to_element(OrderPageLocators.RENT_DATE_INPUT, data.OrderData.rent_date)
        self.click_to_element(OrderPageLocators.EMPTY_PAGE_CLICK)
        self.click_to_element(OrderPageLocators.RENT_PERIOD_DROPDOWN)
        self.click_to_element(locator_rent_day)
        self.click_to_element(OrderPageLocators.SCOOTER_COLOR_BLACK)
        self.add_text_to_element(OrderPageLocators.COMMENT_INPUT, data.OrderData.comment)

    @allure.step("Нажатие на кнопку заказа после заполнения всех данных и подтверждение заказа")
    def order_confirmation(self):
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)
        self.click_to_element(OrderPageLocators.ORDER_YES_BUTTON)

    @allure.step("Проверка текста в всплывающем окне успешного заказа")
    def check_order(self):
        return self.get_text_from_element(OrderPageLocators.ORDER_COMPLETE_LOCATOR)

    @allure.step("Клик на кнопку 'заказать'")
    def click_to_order_button(self, locator):
        self.click_to_element(locator)

