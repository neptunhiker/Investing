import pandas as pd

class Portfolio:

    def __init__(self, name, id, owner):
        self.name = name
        self.aum = 0
        self.id = id
        self.owner = owner
        self.holdings = pd.DataFrame()

    def load(self, location):
        self.holdings = pd.read_csv("../Data/test-data.csv")



class Investor:

    def __init__(self, first_name, last_name):
        self.name = first_name + " " + last_name
        self.portfolios = {}

    def set_up_pf(self, portfolio):
        self.portfolios[portfolio.id] = portfolio