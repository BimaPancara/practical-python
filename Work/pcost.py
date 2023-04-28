# pcost.py
#
# Exercise 1.27
import sys

def portfolio_cost(filename):
    import csv
    read_portfolio = open('Data/portfolio.csv')

    total_cost = 0.0
    
    with read_portfolio as read:
        rows = csv.reader(read_portfolio)
        headers = next(rows)
        for row in rows:
            shares = int(row[1])
            price = float(row[2])
            total_cost += shares*price
            
        return total_cost

if len(sys.argv) ==2:
    filename = sys.argv[1]
else:
    filename='Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total Cost:', cost)