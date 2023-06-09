import stock
import fileparse

class Portfolio:
    # def __init__(self,holdings) -> None:
    #     self._holdings = holdings

    def __init__(self) -> None:
        self.holdings = []

    def append(self,holding):
        if not isinstance(holding, stock.Stock):
            raise TypeError('Expect a Stock instance')
        self.holdings.append(holding) 
        
    @classmethod
    def from_csv(cls,lines,**opts):
        self = cls()
        prodicts = fileparse.parse_csv(lines,select=['name','shares','price'],types=[str,int,float],**opts)
        for d in prodicts:
            self.append(stock.Stock(**d))
        return self

    def __iter__(self):
        return self._holdings.__iter__()
    
    def __len__(self):
        return len(self._holdings)
    
    def __getitem__(self,index):
        return self._holdings[index]
    
    def __contains__(self,name):
        return any([s.name == name for s in self._holdings])
    
    @property
    def total_cost(self):
        # return sum([s.cost for s in self._holdings])
        return sum((s.cost for s in self._holdings))
    
    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares
    
