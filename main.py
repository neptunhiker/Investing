from investment_objects import Portfolio
from investment_objects import Investor

# set up the investor
inv = Investor(first_name="Robert", last_name="Robinson")

# create portfolios and assign to investor
pf01 = Portfolio(name="my first portfolio", id="xyz123", owner=inv)
pf02 = Portfolio(name="my second portfolio", id="abc123", owner=inv)

# load test data into pf
pf01.load()

# print pf holdings
print(pf01.holdings)

# print all portfolios of investor
for key, value in inv.portfolios.items():
    print("Portfolio ID: " + key)
    print("Portfolio name: " + value.name)
    print("Portfolio owner: " + value.owner.name)
    print("-" * 30)
