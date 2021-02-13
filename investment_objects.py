import logging

import pandas as pd

logging.basicConfig(filename="portfolio_logger.log",level=logging.DEBUG, filemode="a", datefmt='%d-%b-%y %H:%M:%S',
                    format='%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s')

class Portfolio:

    def __init__(self, name, id, owner):
        self.name = name
        self.aum = 0
        self.id = id
        self.owner = owner
        self.holdings = pd.DataFrame()

        owner._set_up_pf(portfolio=self)

        logging.info("Portfolio '" + self.name + "' instantiated.")

    def load(self, location=None):

        if location is None:
            location = "Data/testd-data.csv"

        try:
            self.holdings = pd.read_csv(location, sep=None, engine="python")
            logging.info("Security holdings from " + location + " loaded into portfolio '" + self.name + "'.")
        except FileNotFoundError as err:
            logging.info(err)



class Investor:

    def __init__(self, first_name, last_name):
        self.name = first_name + " " + last_name
        self.portfolios = {}

    def _set_up_pf(self, portfolio):
        self.portfolios[portfolio.id] = portfolio