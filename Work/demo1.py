import timethis
import time
class Date:
    def __init__(self,year, month, day) -> None:
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def today(cls):
        tm = time.localtime()
        return cls(tm.tm_year,tm.tm_mon,tm.tm_mday)

class NewDate(Date):
    pass

class Foo(object):
    @staticmethod
    def boo(x):
        print('x=',x)

def logged(func):
    def wwrapper(*args, **kwargs):
        print('calling ',func.__name__)
        print('args ',args)
        print('kwargs',kwargs)
        return func(*args, **kwargs)
    return wwrapper

# @logged
@timethis.timethis
def add(x,y):
    return x+y

@timethis.timethis
def addn(n):
    s = 0
    while n > 0:
        s += n
        n -= 1
    # print(s)

    return s

if __name__ == '__main__':
    a = addn(10000000)

    print('restul is ',a)