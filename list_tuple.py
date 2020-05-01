months = ("January","February","March","April","May","June","July","August","September","October","November","December")
birthday = input("Enter your birthdat in thr format of DD-MM-YYYY:")
index = int(birthday[3:5])-1
bd = months[index]
print("Your birthday month : ",bd)
