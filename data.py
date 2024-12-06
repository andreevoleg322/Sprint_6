from faker import Faker

class Urls:
    URL_MAIN_PAGE = 'https://qa-scooter.praktikum-services.ru/'
    URL_ORDER_PAGE = 'https://qa-scooter.praktikum-services.ru/order'
    URL_DZEN_PAGE = 'https://dzen.ru/?yredirect=true'

class OrderData:
    fake = Faker('ru_RU')

    first_name = fake.first_name()
    last_name = fake.last_name()
    address = fake.address()[:49].replace('/', ' ').replace('(', '').replace(')', '')
    phone = fake.phone_number().replace(' ', '').replace('-', '').replace('(', '').replace(')', '')

    date = fake.date_this_year()
    rent_date = date.strftime('%d.%m.%Y')
    words = fake.words(nb=5, ext_word_list=None)
    comment = ' '.join(words)

class Answers:
    ANSWER_1 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    ANSWER_2 = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
    ANSWER_3 = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    ANSWER_4 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    ANSWER_5 = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    ANSWER_6 = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
    ANSWER_7 = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    ANSWER_8 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

class HeadingTextMainPage:
    heading_text = 'Самокат'
    '\nна пару дней'
    '\nПривезём его прямо к вашей двери,'
    '\nа когда накатаетесь — заберём'