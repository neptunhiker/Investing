import pickle
import logging

import pandas as pd

logging.basicConfig(filename="portfolio_logger.log",level=logging.DEBUG, filemode="w", datefmt='%d-%b-%y %H:%M:%S',
                    format='%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s')

class Portfolio:

    def __init__(self, name, id, owner):
        self.name = name
        self.aum = 0
        self.id = id
        self.owner = owner
        self.holdings = pd.DataFrame()

        logging.info("Portfolio '" + self.name + "' instantiated.")

        self.owner._set_up_pf(portfolio=self)




    def load(self, location=None):

        if location is None:
            location = "Data/testd-data.csv"

        try:
            self.holdings = pd.read_csv(location, sep=None, engine="python")
            logging.info("Security holdings from " + location + " loaded into portfolio '" + self.name + "'.")
        except FileNotFoundError as err:
            logging.info("Portfolio data at '" + location + "' could not be found.")
            logging.error(err)


class Investor:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.name = first_name + " " + last_name
        self.portfolios = {}
        logging.info("Investor '" + self.name + "' instantiated.")



    def _set_up_pf(self, portfolio):
        self.portfolios[portfolio.id] = portfolio
        logging.info("Portfolio '" + portfolio.name + "' set up for " + self.name + ".")