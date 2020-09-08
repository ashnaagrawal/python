n = int(input("Enter the number"))
temp = n
sum = 0
while n>0:
    r =int(n%10) 
    sum += r**3
    n //= 10

if(temp == sum):
    print("Number is armstrong")
else:
    print("Number is not armstrong.")
