"""Парсинг Курса биткойна"""
import requests
import time

from bs4 import BeautifulSoup

from custom_logging import logger


class Currency:

    BTC_USD = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%' \
              'D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD%D0%B0+%D0%B2+%D' \
              '0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0%D1%85&oq=' \
              '&sourceid=chrome&ie=UTF-8'

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/86.0.4240.183 Safari/537.36'}

    current_converted_price = 0
    difference = 100.0

    def init(self):
        self.current_converted_price = float(self.parse_currency())

    def parse_currency(self):
        """Парсит информацию о курсе биткойна"""
        full_page = requests.get(self.BTC_USD, headers=self.headers)

        soup = BeautifulSoup(full_page.content, 'html.parser')

        convert = soup.find("span", class_="DFlfde SwHCTb")
        return float(convert.text.replace(',', ''))

    def check_currency(self):
        """Проверяет чему равен биткоин"""
        currency = float(self.parse_currency())

        if currency >= self.current_converted_price + self.difference:
            print("Курс поднялся, майни Больше!")

        elif currency <= self.current_converted_price - self.difference:
            print("Сейчас курс сильно просел!" + str(currency))
        print(' Сейчас курс 1 BTC = ' + str(currency))
        time.sleep(1)

    @logger.catch
    def run(self):
        """Стартует"""
        self.check_currency()


if __name__ == '__main__':
    currency = Currency()
    currency.run()
