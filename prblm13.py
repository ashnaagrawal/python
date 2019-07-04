#!/usr/bin/python3

import datetime
import subprocess
import sys as s

currentTime=datetime.datetime.now()
currentTime.hour

print("Enter your name:")
x=input()

if currentTime.hour <12:
	z="hii"+x+"Good Morning"
elif currentTime.hour <6:
	z="hii"+x+"Good Afternoon"
else :
	z="hii"+x+"Good Evening"

def execute_unix(inputcommand):
   p = subprocess.Popen(inputcommand, stdout=subprocess.PIPE, shell=True)
   (output, err) = p.communicate()
   return output 

# create wav file
# w = 'espeak -w temp.wav "%s" 2>>/dev/null' % a  
# execute_unix(w)

# tts using espeak
c = 'espeak -ven+f3 -k5 -s150 --punct="<characters>" "%s" 2>>/dev/null' % z 
execute_unix(c)

print("Enter 1 for addition of two numbers:")
print("Enter 2 for sorting of numbers:")
print("Enter 3 for printing list of running modules on your python:")

n=input()

if n=='1':
	print("Enter first number:")
	i1=int(input())
	print("Enter second number:")
	i2=int(input())
	o=i1+i2
	print("sum=",o)
elif n=='2':
	arr=[]
	sn=int(input("Enter the size of the list:\n"))

	for i in range(sn):
		x=int(input())
		arr.append(x)
	arr.sort()
	print(arr)

elif n=='3':
	x=s.modules.keys()
	print(x)	


else :
	print("You entered wrong choice")








