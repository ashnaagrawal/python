number = input("Type a number:")

try:
    number = float(number)
    print("THe number is:", number)
except:
    print("Invalid number")
