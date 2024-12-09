from selenium.webdriver.common.by import By

class OrderPageLocators:

    #локаторы для первой формы
    FIRST_NAME_INPUT = By.XPATH, '//input[@placeholder="* Имя"]' #поле ввода "Имя"
    LAST_NAME_INPUT = By.XPATH, '//input[@placeholder="* Фамилия"]' #поле ввода "Фамилия"
    ADDRESS_INPUT = By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]' #поле ввода "Адрес"
    METRO_STATION_INPUT = By.XPATH, '//input[@placeholder="* Станция метро"]' #строка "Станция метро"
    FIRST_STATION_CHOSE = By.XPATH, ("//input[@placeholder='* Станция метро']/"
                                          "parent::div[@class='select-search__value']/"
                                          "following::*[contains(text(), '") + 'Бульвар Рокоссовского' + "')]"  #выбор первой станции
    PHONE_INPUT = By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]' #поле ввода Телефон"
    NEXT_BUTTON = By.XPATH, '//button[text()="Далее"]' #кнопка "Далее"

    #локаторы для второй формы
    RENT_DATE_INPUT = By.XPATH, '//input[@placeholder="* Когда привезти самокат"]' #строка "Когда привезти самокат
    TODAY_CALENDAR_LOCATOR= By.XPATH, "//div[contains(@class, 'react-datepicker__day--today')]"  # сегодняшний день в выпадающем календаре
    RENT_PERIOD_DROPDOWN = By.XPATH, "//div[text()='* Срок аренды']" #выпадающий список "Срок аренды"
    RENT_PERIOD_OPTION_ONEDAY = By.XPATH, "//*[@class='Dropdown-option' and contains(text(), 'сутки')]" #выбор срока аренды "сутки"
    RENT_PERIOD_OPTION_TWODAYS = By.XPATH, "//*[@class='Dropdown-option' and contains(text(), 'двое суток')]" #выбор срока аренды "двое суток"
    SCOOTER_COLOR_BLACK = By.XPATH, '//label[@for="black"]' #выбор черного самоката
    SCOOTER_COLOR_GREY = By.XPATH, '//label[@for="grey"]' #выбор серого самоката
    COMMENT_INPUT = By.XPATH, '//input[@placeholder="Комментарий для курьера"]' #комментарий для курьера
    ORDER_BUTTON = By.XPATH, '//div[contains(@class, "Order_Buttons")]/button[text()="Заказать"]' #кнопка "Заказать"
    ORDER_YES_BUTTON = By.XPATH, "//button[contains(text(), 'Да')]" #кнопка "Да" в всплывающем окне подтверждения заказа
    ORDER_COMPLETE_LOCATOR = By.XPATH, "//div[text()='Заказ оформлен']"  #надпись "Заказ оформлен"
    BUTTON_CHECK_STATUS_ORDER = By.XPATH, "//button[text()='Посмотреть статус']"  #кнопка "Посмотреть статус"
    EMPTY_PAGE_CLICK = By.XPATH, '//body'  # для клика в пустое место на странице
