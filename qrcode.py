#!/usr/bin/python3


import pyqrcode
urllist=[]
num=input("Enter the number of url:")
x=int(num)
for i in range(x):

	n=input("Enter the web address for qr code foration:")
	urllist.append(n)
	print(urllist)
	for j in n:
#generate qr code
		url=pyqrcode.create(n)
#create and save the png file namin "myqr.png"
		url.svg(n+".svg", scale=3)
		
