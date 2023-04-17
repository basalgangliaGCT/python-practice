import stock
import fileparse

with open('data/portfolio.csv') as lines:
    portdicts = fileparse.parse_csv(lines,select=['name','shares','price'],types=[str,int,float])

print('portdicts \n', portdicts)

portfolio = [stock.Stock(d['name'],d['shares'],d['price']) for d in portdicts]

ms = sum([s.cost() for s in portfolio])

print('the summary of cost is:' , ms)
print(f'the summary of cost is: {ms}')
print('the summary of cost is: %.2f' % ms)

