#!/usr/bin/python3

import time


print("Enter your name :")
n=input()
print("Enter your age :")
a=int(input())
y=95-a 
print(f'{n} you will turn 95 in year',time.localtime().tm_year+y)

