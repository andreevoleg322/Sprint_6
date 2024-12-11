from selenium.webdriver.common.by import By


class MainPageLocators:
    #локаторы FAQ
    LAST_QUESTION_LOCATOR = By.XPATH, "//div[@aria-controls='accordion__panel-7']"  # локатор последнего вопроса, до которого надо скроллить
    QUESTION_LOCATOR = By.XPATH, "//div[@aria-controls='accordion__panel-{}']"  # выпадающее поле с вопросами
    ANSWER_LOCATOR = By.ID, "accordion__panel-{}" # выпадающее поле с ответами

    #локаторы создания заказа
    ORDER_BUTTON_UP = By.XPATH, '//button[text()="Заказать"]' #кнопка "Заказать" вверху
    ORDER_BUTTON_DOWN = By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]' #кнопка "Заказать" внизу

    #локаторы общего назначения
    BUTTON_COOKIE_ACCEPT_LOCATOR = By.XPATH, "//button[text()='да все привыкли']"  # кнопка куков

    #локаторы для работы с логотипами
    LOGO_SCOOTER = By.XPATH, '//a[contains(@class, "Header_LogoScooter")]' #логотип самоката
    LOGO_YANDEX = By.XPATH, '//a[contains(@class, "Header_LogoYandex")]' #логотип Яндекса
    HEADING_TEXT = By.CLASS_NAME, "Home_Header__iJKdX"  # заголовок страницы "Самокат на пару дней"