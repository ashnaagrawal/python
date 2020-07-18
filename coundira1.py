def printFirstRepeating(numbersArray, n): 
    Min = -1
    myset = dict() 
    for i in range(n - 1, -1, -1): 
        if numbersArray[i] in myset.keys(): 
            Min = i 
        else: 
            myset[numbersArray[i]] = 1

    if (Min != -1): 
        print("The first repeating element is", numbersArray[Min]) 
    else: 
        print("There are no repeating elements") 

n = int(input())
numbersArray = []
for i in range(n):
    number = int(input())
    numbersArray.append(number)  

n = len(numbersArray) 
printFirstRepeating(numbersArray, n)