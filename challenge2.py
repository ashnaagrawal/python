import random

colors = ["black","white","yellow","brown","blue","grey","orange","green","purple","red","pink"]

while True :
    color = colors[random.randint(0,len(colors) - 1)]
    guess = input("I'm thinking about a color, can u guess it ?")

    while True:
        if (color == guess.lower()):
            break
        else :
            guess = input("Nope. Try again :")

    print("You guessed it! I was thinking about", color)

    play_again = input("Let's play again ? Type 'no' to quit OTHERWISE press ENTER")

    if play_again.lower() == 'no' :
        break

print("It was fun , thanks for playing!!!")
        

