import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Поиск элемента с ожиданием")
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Клик по элементу")
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        self.find_element_with_wait(locator).click()

    @allure.step("Прокрутка до элемента")
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Ввод текста в элементе")
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step("Получение текста в элементе")
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step("Форматирование элемента")
    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return (method, locator)

    @allure.step("Получение текущего адреса страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Переключение вкладки")
    def switch_tab(self):
        return self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Ожидание загрузки страницы")
    def wait_loading_site(self, url):
        WebDriverWait(self.driver, 5).until(expected_conditions.url_to_be(url))
