import math

m = int(input())
t = int(input())
r = float(input())

if(m>0 and t>=0 and r>=0):
    ra = m
    for i in range(0,t):
        amount = ra/(1+r/float(1200))
        interest = ra - amount
        
        ra = ra + (m-interest)
    finalamount = math.ceil(amount-0.5)   
    if(finalamount>ra):
        print(finalamount)
        finalamount = math.ceil(ra)
    else:
        print(finalamount)
        finalamount = math.floor(ra)



      

