from typedproperty import typedproperty

class Stock:
    x = 42
    name = typedproperty('name',str)
    shares = typedproperty('shares',int)
    price = typedproperty('price', float)

    __slots__ = ('_name','_shares','_price')
    def __init__(self,name,shares,price) -> None:
        self.name = name
        self.shares = shares
        self.price = price

    # @property
    # def shares(self):
    #     return self._shares
    
    # @shares.setter
    # def shares(self,shares):
    #     if not isinstance(shares,int):
    #         raise TypeError('Expected --- int')
    #     self._shares = shares

    @property    
    def cost(self):
        return self.shares * self.price
    
    def sell(self, num):
        self.shares -= num

    def __repr__(self) -> str:
        return f"Stock('{self.name}', {self.shares}, {self.price})"
    
class MyStock(Stock):
    def __init__(self, name, shares, price, factor) -> None:
        super().__init__(name, shares, price)
        self.factor = factor

    def cost(self):
        # return 1.25 * self.shares * self.price
        # return self.factor * super().cost()
        return self.factor * super().cost
    
    def panic(self):
        self.sell(self.shares)

class NewStock(Stock):
    @property
    def yow(self):
        print('Yow!')

def main(argv):
    import fileparse

    with open('data/portfolio.csv') as lines:
        portdicts = fileparse.parse_csv(lines,select=['name','shares','price'],types=[str,int,float])

    print('portdicts \n', portdicts)

    portfolio = [Stock(d['name'],d['shares'],d['price']) for d in portdicts]

    ms = sum([s.cost() for s in portfolio])

    print('the summary of cost is:' , ms)
    print(f'the summary of cost is: {ms}')
    print('the summary of cost is: %.2f' % ms)
    return

if __name__ == '__main__':
    import sys
    main(sys.argv)

