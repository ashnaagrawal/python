blog_posts = ["","The 10 coolest math functions in python","How to make HTTp request in Python","","A tutorial about data types in Python"]

for post in blog_posts:
    if post == "":
        continue
    else:
        print(post)

print("-------------------------------")

myString = "This is a String"

for char in myString:
    print(char)


print("--------------------------")

for x in range(0,10):
    print(x)

print("----------------------------")

person  = {"name":"Ayansh","Age":"20","Gender":"Male"}

for key in person:
    print(key,":",person[key])
print("-----------------------------------------------------")
   
