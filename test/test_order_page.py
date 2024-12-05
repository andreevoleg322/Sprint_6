import pytest
import allure
from conftest import driver
import data
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators


class TestOrderPage:

    @pytest.mark.parametrize(
        'locator, order_data, rent_day',
        [
            (MainPageLocators.ORDER_BUTTON_UP, data.OrderData, OrderPageLocators.RENT_PERIOD_OPTION_ONEDAY),
            (MainPageLocators.ORDER_BUTTON_DOWN, data.OrderData, OrderPageLocators.RENT_PERIOD_OPTION_TWODAYS)

        ]
    )

    @allure.title('Проверка заказа самоката из двух точек входа')
    def test_create_order(self, driver, locator, order_data, rent_day):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_to_element(MainPageLocators.BUTTON_COOKIE_ACCEPT_LOCATOR)
        main_page.click_to_order_button(locator)
        order_page.set_order_form_1()
        order_page.set_order_form_2(rent_day)
        order_page.order_confirmation()
        assert 'Заказ оформлен' in main_page.check_order(OrderPageLocators.ORDER_COMPLETE_LOCATOR)