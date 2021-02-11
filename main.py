from investment_objects import Portfolio


pf = Portfolio("my first portfolio", "xyz123", "Sebastian")

pf.load(location="../Data/test-data.csv")
print(pf.holdings)