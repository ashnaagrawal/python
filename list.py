#!/usr/bin/python3

#defining tuple
t=(1,56,33,11,78)
print(t)   #printing tuple 
print(t[0:2]) #printing elements of tuple

#defining list
l=[34,66,55,78,24]
print(l)         #printing list
print(l[0:3])    #printing elements of list

l.insert(3,'hello')   #inserting elements in list
print(l)

l.append('66666')     #append elements in list
print(l)

print(type(l))

l.append(t) 
print(l)       #appending tuple in list
 
