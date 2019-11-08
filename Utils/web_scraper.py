import requests
import bs4
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import os
import datetime


class StockData:

    def __init__(self, stock_symbol):
        self.stock_symbol = stock_symbol
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.options)
        self.options_url = 'https://finance.yahoo.com/quote/{}/options?p={}'.format(self.stock_symbol,
                                                                                    self.stock_symbol)

    def __load_options_page(self):
        self.driver.get(self.options_url)
        delay = 3
        try:
            WebDriverWait(self.driver, delay).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'calls'))
            )
            html = self.driver.page_source
            return BeautifulSoup(html, 'lxml')
        except TimeoutException:
            return None

    def __close_driver(self):
        self.driver.quit()

    def __strip_commas(self, number):
        if number != '-':
            return number.replace(',', '')
        else:
            return 0

    def __calculate_vpm_price(self, open_interest_list, strike_oi_product_list):
        print(open_interest_list)
        print(strike_oi_product_list)
        oi = sum(open_interest_list)
        strike_oi = sum(strike_oi_product_list)
        if oi == 0:
            return 0
        else:
            return strike_oi / oi

    def __calculate_precent_from_current(self, vpm, current):
        return ((vpm - current) / current) * 100

    def get_date_options(self):
        date_list = {}
        soup = self.__load_options_page()
        if soup is not None:
            date_select = (soup.find('select', attrs={'class': 'Fz(s)'}))
            for date in date_select.findAll('option'):
                date_list[date.text] = date['value']
            self.__close_driver()
            return date_list
        else:
            return None

    def get_call_data(self, utc_date):
        data_list = []
        url = 'https://finance.yahoo.com/quote/{}/options?date={}&p={}'.format(self.stock_symbol, utc_date, self.stock_symbol)
        self.driver.get(url)
        WebDriverWait(self.driver, 5)
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'lxml')

        price = soup.find('span', {'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})
        current_price = float(price.text)

        table = soup.find('table', attrs={'class': 'calls'})
        rows = self.get_table_rows(table)

        vpm = self.get_vpm(rows)
        percent_from_current = self.__calculate_precent_from_current(vpm, current_price)

        data_list.append(self.stock_symbol)
        data_list.append(str(current_price))
        data_list.append(str(round(vpm, 2)))
        data_list.append(str(round(percent_from_current, 3)))

        return data_list

    def get_table_rows(self, table):
        body = table.find('tbody')
        return body.findAll('tr')

    def get_vpm(self, rows):
        strike_list = []
        oi_list = []
        product_list = []
        for row in rows:
            strike = float(self.__strip_commas(row.find('td', attrs={'class': 'data-col2'}).text))
            oi = int(self.__strip_commas(row.find('td', attrs={'class': 'data-col9'}).text))
            strike_list.append(strike)
            oi_list.append(oi)
            product_list.append(strike * oi)

        vpm = self.__calculate_vpm_price(oi_list, product_list)
        self.driver.quit()
        return vpm
