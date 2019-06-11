#!usr/bin/python3

l1=[1,2,3,1,4,5,66,22,2,6,0,9]
x=[]
y=[]
print("Numbers less than 5 in list are :")

for i in l1:
	if i > 5:
		print(i)
		x.append(i)
print("Numbers <=2 in list are:")

for i in l1:
	if i<=2:
		print(i)
		y.append(i)

print("list 1 is",x)
print("list 2 is",y)

