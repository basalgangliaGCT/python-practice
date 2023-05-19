

# import heapq
# def heapsort(iterable):
#     h = []
#     for value in iterable:
#         heapq.heappush(h, value)
#     return [heapq.heappop(h) for i in range(len(h))]
# print(heapsort([4,5,2,1,6,345,3,43,3]))
# print(sorted([4,5,2,1,6,345,3,43,3]))


# from collections import deque
# def roundrobin(*iterables):
#     "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
#     iterators = deque(map(iter, iterables))
#     while iterators:
#         try:
#             while True:
#                 yield next(iterators[0])
#                 iterators.rotate(-1)
#         except StopIteration:
#             # Remove an exhausted iterator.
#             iterators.popleft()
# aa = roundrobin('ABC','D','EF')
# for i in aa:
#     print(i)

# a = ['one','two','three']
# print('a: ',a)
# print('*a: ',*a)
# def po(*para):
#     print('para: ',para)
#     print('type of para',type(para))
# po(a)


# from collections import deque
# import itertools
# def moving_average(iterable, n=3): #按从左到右的顺序，求iterable中n个数的平均值
#     # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
#     # https://en.wikipedia.org/wiki/Moving_average
#     it = iter(iterable)
#     # print('0: ',list(it))
#     d = deque(itertools.islice(it, n-1))
#     print('1: ', d)
#     d.appendleft(0)
#     print('2: ',d)
#     s = sum(d)
#     print('3: ', s)
#     for elem in it:
#         print('4: ', elem)
#         s += elem - d.popleft()
#         print('5: ', s)
#         d.append(elem)
#         print('6: ', d)
#         print('7:', s/n)
#         yield s / n
# a = [40, 30, 50, 46, 39, 44]
# kk = moving_average(a)
# for i in kk:
#     print(i)


# class Color(object):
#     def __init__(self):
#         self.index = -1
#         self.colors = ['red', 'white', 'black', 'green']
#     def __iter__(self):
#         self.index = -1
#         return self
#     def __next__(self):
#         self.index += 1
#         if self.index >= len(self.colors):
#             raise StopIteration
#         return self.colors[self.index]
# cc = Color()
# c1 = iter(cc)
# c2 = iter(cc)
# print('c1 is c2' if id(c1) == id(c2) else 'c1 is not c2')
# lst = [1, 2, 3]
# class ListIterator:
#     def __init__(self, lst):
#         self.lst = lst
#         self.index = -1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.index += 1
#         if self.index > len(self.lst):
#             raise StopIteration
#         return self.lst[self.index]
# ll = ListIterator(lst)
# l1 = iter(ll)
# l2 = iter(ll)
# print('l1 is l2' if id(l1) == id(l2) else 'l1 is not l2')
# def my_iter(lst):
#     return ListIterator(lst)
# kk = my_iter(lst)
# k1 = iter(kk)
# k2 = iter(kk)
# print('k1 is k2' if id(k1) == id(k2) else 'k1 is not k2')
# t1 = iter(lst)
# t2 = iter(lst)
# print('t1 is t2' if id(t1) == id(t2) else 't1 is not t2')


# def fab(max):
#     n,a,b = 0,0,1
#     while n < max:
#         yield b
#         a,b = b,a+b
#         n += 1
# for i in fab(5):
#     print(i)
# from inspect import isgeneratorfunction
# print('fab is a generator function' if isgeneratorfunction(fab) else 'fab is not a generator function')
# import types
# print('fab is a generator type' if isinstance(fab,types.GeneratorType) else 'fab is not a generator type')
# print('fab(5) is a generator type' if isinstance(fab(5),types.GeneratorType) else 'fab(5) is not a generator type')
# from collections.abc import Iterable
# print('fab is iterable' if isinstance(fab,Iterable) else 'fab is not iterable')
# print('fab(5) is iterable' if isinstance(fab(5),Iterable) else 'fab(5) is not iterable')
# from collections.abc import Iterator
# print('fab is a itertor' if isinstance(fab,Iterator) else 'fab is not a iterator')
# print('fab(5) is a iterator' if isinstance(fab(5),Iterator) else 'fab(5) is not a iterator')
# print(next(fab(5)))


# from collections import deque
# def mtail(filename,n=10):
#     with open(filename) as lines:
#         return deque(lines,n)
# ret = mtail('data.txt')
# for i in ret:
#     print(i,end='')