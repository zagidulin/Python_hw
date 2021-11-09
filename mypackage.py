import requests
from bs4 import BeautifulSoup


# базовая формула: price_per_tone = 16*(цена нефти, usd) + (затраты на производство, usd)
def pricing(oil_price, eur_usd, prod_cost):
    '''
    Функция для опреления базовой стоимости ВБП
    Входные параметры:
        - oil_price - float, стоимость нефти на момент расчёта;
        - eur_usd - float, курс евро в долларах США на момент расчёта;
        - prod_cost - int, затраты на производство ВБП, в евро
    '''
    price = round(oil_price*16 + prod_cost/eur_usd, 2)
    return price


class Pricer():
    '''
    Класс для опреления стоимости ВБП для всех клиентов
    Входные параметры:
        - customers - dict
            словарь установленной формы с информацией о Клиентах:
                customers = {
                    client name (str):{
                        'location': str, одно из двух значений: 'EU' или 'CN' - для клиентов из Евросоюза или Китая соответственно,
                        'volumes': int, объём ежемесечного заказа или скользящая средняя объёмов заказа за последние 3 месяца,
                        'comment': str, комментарий о том как определён 'volumes': 'monthly' или 'moving_average'.
                    };
                }
        - discounts - dict
            словарь установленной формы с шкалой скидок от объёма:
                discounts = {'up to 100': float, размер скидки
                             'up to 300': float, размер скидки
                             '300 plus': float}   размер скидки
        - eu_log_cost - int, float
            затраты на доставку клиентам из EU, в евро;
        - cn_log_cost - int, float
            затраты на доставку клиентам из Китая, в долл. США
        - prod_cost - int
            затраты на производство
    '''
    def __init__(self, customers, discounts, eu_log_cost, cn_log_cost, prod_cost):
        self.customers = customers
        self.discounts = discounts
        self.eu_log_cost = eu_log_cost
        self.cn_log_cost = cn_log_cost
        self.prod_cost = prod_cost
        self.urls = {'oil': 'https://quote.rbc.ru/ticker/181206',
                     'eur/usd': 'https://quote.rbc.ru/ticker/59087'}
        
    # Статический метод для избежания дублирования кода в методах get_oil_price и get_eur_usd
    @staticmethod
    def parser(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        return soup
    
    # метод получает стоимость нефти
    def get_oil_price(self):
        oil_price = self.parser(self.urls['oil']).find('span', class_='chart__info__sum').text
        oil_price = oil_price[1:]
        oil_price = float('.'.join(oil_price.split(',')))
        return oil_price
    
    # метод получает курс eur/usd
    def get_eur_usd(self):
        eur_usd = self.parser(self.urls['eur/usd']).find('span', class_='chart__info__sum').text
        eur_usd = eur_usd[1:]
        eur_usd = float('.'.join(eur_usd.split(',')))
        return eur_usd
    
    # метод добавляет скидку в словарь покупателей
    def get_discount(self):
        for customer in self.customers:
            try:
                if self.customers[customer]['volumes'] < 100:
                    self.customers[customer]['dicount'] = 1 - self.discounts['up to 100']
                elif self.customers[customer]['volumes'] < 300:
                    self.customers[customer]['dicount'] = 1 - self.discounts['up to 300']
                else:
                    self.customers[customer]['dicount'] = 1 - self.discounts['300 plus']
            except:
                self.customers[customer]['dicount'] = 1
    
    # метод расчитывает цены для всех покупателей
    def pricing(self):
        prices = dict()
        try:
            eur_usd = self.get_eur_usd()
        except:
            err = 'Курс eur/usd недоступен'
            return err
        try:
            oil_price = self.get_oil_price()
        except:
            err = 'Цена нефти недоступна'
            return err
        self.get_discount()
        for customer in self.customers:
            try:
                location = self.customers[customer]['location']
            except KeyError:
                location = None
            if location == 'EU':
                price = (16 * oil_price + self.eu_log_cost * eur_usd + self.prod_cost * eur_usd) * self.customers[customer]['dicount']
                price = round(price * eur_usd, 2)
                prices[customer] = f'{price} EUR'
            elif location == 'CN':
                price = (16 * oil_price + self.cn_log_cost + self.prod_cost) * self.customers[customer]['dicount']
                price = round(price, 2)
                prices[customer] = f'{price} USD'
            else:
                prices[customer] = f'Нет данных о расположении Клиента' 
        return prices
