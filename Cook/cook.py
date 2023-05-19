
# #1.13
# from operator import itemgetter
# rows = [
#     {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003}, 
#     {'fname': 'David', 'lname': 'Beazley', 'uid': 1002}, 
#     {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}, 
#     {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
# ]
# sf = sorted(rows,key=itemgetter('fname'))
# print('1-0: ', sf)
# sf = sorted(rows,key=lambda r: r['fname'])
# print('1-1: ', sf)
# si = sorted(rows,key=itemgetter('uid'))
# print('2: ', si)
# slf = sorted(rows,key=itemgetter('lname','fname'))
# print('3-0: ',slf)
# slf = sorted(rows,key=lambda r:(r['lname'],r['fname']))
# print('3-1: ', slf)
# print('4-0: ', min(rows,key=itemgetter('uid')))
# print('4-1: ', min(rows,key=lambda r: r['uid']))
# print('5-0: ', max(rows,key=itemgetter('uid')))
# print('5-1: ', max(rows,key=lambda r: r['uid']))

# #1.12
# from collections import Counter
# words1 = [
#     'first','first','first','two','two','three','four'
# ]
# words2 = [
#     'first','two','three','three','four','four','five'
# ]

# w1 = Counter(words1)
# print('1: ', w1)
# top3 = w1.most_common(3)
# print('2: ', top3)
# w2 = Counter(words2)
# print('3: ', w2)
# w1a2 = w1 + w2
# print('4: ', w1a2 )
# w1s2 = w1 - w2
# print('5: ', w1s2)


# #1.10
# def dedup_1(items):
#     set=[]
#     for item in items:
#         if item not in set:
#             set.append(item)
#     return set

# a = [5,1,1,2,3,4,4,5,5,2,3,5,5]
# b = dedup_1(a)
# print(b)

# def dedup_2(items):
#     sset = set()
#     for item in items:
#         if item not in sset:
#             yield item
#             sset.add(item)

# b = dedup_2(a)
# print(*b)

# d = {'name':'tom', 'age':10, 'name':'jery'}
# dd = dedup_2(d)
# print(*dd)

# def dedup_3(items, key=None): 
#     seen = set()
#     for item in items:
#         val = item if key is None else key(item) 
#         if val not in seen:
#             yield item 
#             seen.add(val)
#             # print('seen:',seen)

# a = [{'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
# b = dedup_3(a, key=lambda d: (d['x'],d['y']))
# print(*b)
# b = dedup_3(a, key=lambda d: d['x'])
# print(*b)

# a = [5,1,1,2,3,4,4,5,5,2,3,5,5]
# b=list(set(a)) #don't preserve order
# print(b)

# with open('1.10.data.txt','r') as f:
#     for line in dedup_2(f): #eliminating duplicate line and keep order
#         print(line, end='')  

# #1.9
# a={
#     'x' : 1,
#     'y' : 2,
#     'z' : 3 
# }

# b={
#     'w' : 10,
#     'x' : 11,
#     'y' : 2 
# }

# print('1: ', a.keys() & b.keys())
# print('2: ', a.keys() - b.keys())
# print('3: ', a.items() & b.items())
# print('4: ', {key:a[key] for key in a.keys() - b.keys()})

# #1.8
# prices = {
#     'ACME': 45.23, 
#     'AAPL': 612.78, 
#     'IBM': 205.55, 
#     'HPQ': 37.20, 
#     'FB': 10.75
# }

# print('1: ',min(zip(prices.values(),prices.keys())))
# print('2: ',max(zip(prices.values(),prices.keys())))
# print('3: ',*zip(range(3), ['fee', 'fi', 'fo', 'fum']))

# a=('one','two','three')
# b=[1,2,4]
# c=('aa','bb','cc')
# print('4: ',*zip(a,b))
# print('5: ',list(zip(a,b)))
# print('6: ',*zip(a,b,c))
# print('7: ',list(zip(a,b,c)))
# print('8: ',*zip(*zip(a,b)))

# print('9: ',list(zip(('a', 'b', 'c'), (1, 2, 3), strict=True))) #OK
# # print('10: ',list(zip(('a', 'b', 'c'), (1, 2, 3, 4), strict=True))) #ValueError
# print('11:', sorted(zip(prices.values(),prices.keys())))
# print('12:', sorted(zip(prices.keys(),prices.values())))
# print('13:', min(prices))
# print('14:', min(prices.values()))
# print('15:', min(prices,key=lambda k:prices[k]))
# print('16:', prices[min(prices,key=lambda k:prices[k])])

# example = { 'AAA' : 45.23, 'ZZZ': 45.23 }
# print('17:', min(zip(example.values(),example.keys())))
# print('18:', max(zip(example.values(),example.keys())))

# #1.5
# import heapq
# class Item:
#     def __init__(self, name): 
#         self.name = name
#     def __repr__(self):
#         return 'Item({!r})'.format(self.name)

# class PriorityQueue:
#     def __init__(self) -> None:
#         self._queue = []
#         self._index = 0
#     def push(self,item,priority):
#         heapq.heappush(self._queue,(-priority,self._index,item))
#         self._index += 1
#     def pop(self):
#         return heapq.heappop(self._queue)[-1]

# pq = PriorityQueue()
# pq.push(Item('first'),2)
# pq.push(Item('second'),2)
# pq.push(Item('third'),2)
# print(pq._queue)
# print(pq.pop())

# #1.4
# import heapq
# push = heapq.heappush

# h = []
# push(h, 'one')
# push(h, 'Two')
# push(h, 'three')
# push(h, 'four')
# push(h, 'Five')
# push(h, 'six')
# push(h, 'eight')
# print(h)
# print(heapq.nsmallest(7,h))
# print(sorted(h))
# print(heapq.nsmallest(7,h,key=str.lower))
# print(sorted(h,key=str.lower))


# portfolio = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1}, 
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22}, 
#     {'name': 'FB', 'shares': 200, 'price': 21.09}, 
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75}, 
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35}, 
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
# cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
# expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
# print(cheap)
# print(expensive)

# #1.3
# from collections import deque

# def search(lines, pattern, history=5):
#     previous_lines = deque(maxlen=history)
#     print('1: ',previous_lines)
#     for line in lines:
#         print('2: ',line)
#         if pattern in line:
#             print('3: ',line,previous_lines)
#             yield line, previous_lines
#         previous_lines.append(line)
#         print('4: ',previous_lines)

# if __name__ == '__main__':
#     with open('data.txt') as f:
#         for line, prevlines in search(f, 'AA', 5):
#             for pline in prevlines:
#                 print(pline, end='')
#             print(line, end='')
#             print('-'*20)


# #1.2
# records = [
#     ('foo', 1, 2),
#     ('bar', 'hello'),
#     ('foo', 3, 4), 
# ]
# def do_foo(x, y=None): 
#     print('foo', x, y)

# def do_bar(s): 
#     # print(s)
#     print('bar', s)

# for tag, *args in records:
#     # print(args)
#     # print(*args) 
#     if tag == 'foo':
#         do_foo(args) 
#         do_foo(*args) 
#     elif tag == 'bar':
#         do_bar(args)
#         do_bar(*args)

# line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
# uname, *fields, homedir, sh = line.split(':')
# print(uname)
# print(fields)
# print(*fields)
# print(homedir)
# print(sh)

# record = ('ACME', 50, 123.45, (12, 18, 2012))
# name, *_, (*_, year) = record
# print(name)
# print(year)

# items = [1, 10, 7, 4, 5, 9]
# def sum(items):
#     head, *tail = items
#     return head + sum(tail) if tail else head
# print(sum(items))