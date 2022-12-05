"""
Created on Fri Nov 19 4:32:37 2022

@author: Ankit kumar poddar
"""
#0,1,1,2,3,5,8,13....
limit=int(input("Enter limit"))
a=0
b=1
c=1
print("Fibonacci series")
print(a)
print(b)
while c<=limit:
    print(c)
    a=b#2
    b=c#3
    c=a+b
# -*- coding: utf=8 -*-
import math
# A utility function that will return true
# if a number is a perfect square else, this will return false
def isPerfectSquare(num):
# finding the sqaure root of a number
   s=int(math.sqrt(num))
   return s*s==num
def isFibonacciNumber(n):
#Return true if the number is fibonacci otherwise return false
   return isPerfectSquare(5*n*n+4) or isPerfectSquare(5*n*n-4)
n=int(input('enter the number you want to check:'))
if(isFibonacciNumber(n)==True):
    print('Given number is a fibonnaci number')
else:
    print(n, 'is not a fibonnact number')

