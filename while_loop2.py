number = 6

guess = int(input("I'm thinking about a number between zero and ten. Can you guess it?"))

while True:
    if guess == number:
        break
    else :
        guess = int(input("Nope. Try again :"))
