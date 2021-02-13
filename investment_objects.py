import logging

import pandas as pd

logging.basicConfig(filename="portfolio_logger.log",level=logging.DEBUG, filemode="a", datefmt='%d-%b-%y %H:%M:%S',
                    format='%(asctime)s - level: %(levelname)s - module: %(module)s - function: %(funcName)s - msg: %(message)s')

class Portfolio:

    def __init__(self, name, id, owner):
        self.name = name
        self.aum = 0
        self.id = id
        self.owner = owner
        self.holdings = pd.DataFrame()

        owner._set_up_pf(portfolio=self)

    def load(self, location=None):

        if location is None:
            try:
                self.holdings = pd.read_csv("Data/test-datia.csv", sep=None, engine="python")
            except FileNotFoundError:
                logging.info("damn")
        else:
            try:
                self.holdings = pd.read_csv(location, sep=None)
            except FileNotFoundError:
                pass


class Investor:

    def __init__(self, first_name, last_name):
        self.name = first_name + " " + last_name
        self.portfolios = {}

    def _set_up_pf(self, portfolio):
        self.portfolios[portfolio.id] = portfolio