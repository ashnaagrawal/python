#!/usr/bin/python3

import datetime

currentTime=datetime.datetime.now()
currentTime.hour

print("Enter your name:")
x=input()


if currentTime.hour <12:
	print("hii",x,"Good Morning")
elif currentTime.hour <6:
	print("hii",x,"Good Afternoon")
else :
	print("hii",x,"Good Evening")






