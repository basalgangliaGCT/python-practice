name = 'ex'

def f(name):
   print(name)
   name ='in'
   print(name)
   return

f(name)
print(name)

'''
list = [1,2,3]
def l(list):
   print(list)
   list.append(44)
   print(list)
   return
l(list)
print(list)

list = [1,2,3]
def s():
   list.append(44)
   print(list)
   return
s()
print(list)
'''
list = [1,2,3]
def ss(list):
   list.append(33)
   list=[3,4,5]
   return
ss(list)
print(list)

'''
import csv

def port_cost(mFile):
   mList=[]
   mHandle = open(mFile)
   mRows = csv.reader(mHandle)
   mHandle.close
   next(mRows)
   for i, line in enumerate(mRows,start=1):
      try:
         mList.append({'name':line[0],'shares':int(line[1]),'price':float(line[2])})
      except ValueError:
         if line[1]=='':
            print("Row %d: Couldn't convert:" % i,line)
            line[1]=0
         if line[2]=='':
            print("Row %d: Couldn't convert:" % i,line)
            line[2]=0
         mList.append({'name':line[0],'shares':int(line[1]),'price':float(line[2])})
   mTotal = 0   
   for mItem in mList:
      mTotal = mTotal + mItem['shares']*mItem['price']
   return mList
   


def report(mPortfolio,mPrice):
   mReport = []
   print('%10s %10s %10s %10s' %('Name','Shares','Price','Change'))
   a='-'
   print(a*44)
   for i in mPortfolio:
      mName = i['name']
      mShares = i['shares']
      mInitPrice = i['price']
      mCurrentPrice = mPrice[mName]
      mChange = mCurrentPrice - mInitPrice
      mReport.append({'name':mName,'shares':mShares,'price':mCurrentPrice,'change':mChange})
   
   for i in mReport:
      (name, shares, price, change) = tuple(i.values())
      print(f'{name:<10s}{shares:10d}${price:10.2f}{change:10.2f}')
   
   return mReport
   
def getPrice(mFile):
   mPrice={}
   mHandle = open(mFile)
   mRows = csv.reader(mHandle)
   mHandle.close
   #next(mRows)
   for mRow in mRows:
      #print(mRow)
      try:
         mPrice[mRow[0]]=float(mRow[1])
      except IndexError:
         pass
   return mPrice

def getPortfolio(fName):
   mList=[]
   mHandle = open(fName)
   mRows = csv.reader(mHandle)
   mHandle.close
   next(mRows)
   for line in mRows:
      try:
         mList.append({'name':line[0],'shares':int(line[1]),'price':float(line[2])})
      except ValueError:
         if line[1]=='':
            line[1]=0
         if line[2]=='':
            line[2]=0
         mList.append({'name':line[0],'shares':int(line[1]),'price':float(line[2])})
   mTotal = 0   
   for mItem in mList:
      mTotal = mTotal + mItem['shares']*mItem['price']
   return mList
'''   

'''
import csv

def getList(fName):
   mList=[]
   mHandle = open(fName)
   mRows = csv.reader(mHandle)
   mHandle.close
   next(mRows)
   for line in mRows:
      try:
         mList.append((line[0],int(line[1]),float(line[2])))
      except ValueError:
         if line[1]=='':
            line[1]=0
         if line[2]=='':
            line[2]=0
         mList.append((line[0],int(line[1]),float(line[2])))
   mTotal = 0   
   for mName, mShares, mPrice in mList:
      mTotal = mTotal + mShares*mPrice
   return mTotal
   
'''
'''
def countT(fName):
   'count total from the file'
   mTotal = 0
   with open(fName,'rt') as mFile:
      next(mFile)
      for line in mFile:
         mList = line.split(',')
         try:
            mTotal = float(mList[1])*float(mList[2]) + mTotal
         except ValueError:
            print('count not convert',line)
   return mTotal

'''
'''
import sys

fName = sys.argv[1]
print('file name:',fName)
print(countT(fName))
'''

'''

import csv
f = open('data\missing.csv')
cc = csv.reader(f)
header = next(cc)
mTotal = 0
for i in cc:
   #mList = i.split(',')
   print(i)
   try:
      mTotal = float(i[1])*float(i[2]) + mTotal
   except ValueError:
      print('could not convert',i)
f.close()
print(mTotal)
'''
