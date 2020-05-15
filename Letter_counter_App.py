print("Welcome to the Letter Counter App \n")
name = input("What is your name :")
print("Hello"+" "+name+'!')
print("\nI will count the number of timies that a specific letter occurs in a message.\n")

msg = input("Please enter a message :")

letter = input("Which letter would you like to count the occurence of : ")
msg = msg.lower()
letter = letter.lower()

letter_count = msg.count(letter)

print("\n"+name+" "+"Your message has"+" "+ str(letter_count) + " "+letter+"'s in it" )
