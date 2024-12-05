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
