import time as t
import matplotlib.pyplot as plt

print("THis program will check the speed of the programmer")
print("The word you have to type 'programming' as fast as you can for five times")

input("Press the enter to contine:")

mistakes = 0
times = []


while len(times)<5:
    start = t.time()
    word = input("Type the word : ")
    end = t.time()
    time_elapsed = end - start

    times.append(time_elapsed)

    if(word.lower() != "programming"):
        mistakes += 1

print("you made" ,mistakes, "mistakes")
print("Time taken :", time_elapsed)
print("You started at :",start)
print("You ended at :",end)
print("Time taken for each word :",times)

print("Now let's see your evaluation : ")

t.sleep(3)

x = [1,2,3,4,5]
y = times
plt.plot(x,y)
legend = ["1","2","3","4","5"]
plt.xticks(x,legend)
plt.xlabel("Number of attempts")
plt.ylabel("Time in seconds")
plt.title("Your typing evolution")
plt.show()
    
    


