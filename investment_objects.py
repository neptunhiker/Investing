import pandas as pd

class Portfolio:

    def __init__(self, name, id, owner):
        self.name = name
        self.aum = 0
        self.id = id
        self.owner = owner
        self.holdings = pd.DataFrame()

        owner._set_up_pf(portfolio=self)

    def load(self, location):
        self.holdings = pd.read_csv(location, sep=None)



class Investor:

    def __init__(self, first_name, last_name):
        self.name = first_name + " " + last_name
        self.portfolios = {}

    def _set_up_pf(self, portfolio):
        self.portfolios[portfolio.id] = portfolio