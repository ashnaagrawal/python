N = int(input())

# find the number of Rs.5 coins
five = int((N-4)/5)

# find the number of Rs.1 coins
if((N-5*five) %2==0):
    one = 2
else:
    one = 1

# find the number of Rs.2 coins
two = int((N - (5*five + 1*one))/2)

coins = (five+one+two)

print(coins,five,two,one)
