# pcost.py
#
# Exercise 1.27

read_portfolio = open('Data/portfolio.csv', 'rt')

total_cost = 0.0
    
with read_portfolio as read:
    headers = next(read_portfolio)
    for line in read:
        row = line.split(',')
        shares = int(row[1])
        price = float(row[2])
        total_cost += shares*price
            
    print(total_cost)
