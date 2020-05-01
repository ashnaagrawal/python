data = {'name':'Ashna','gender':'female','age':'20','address':'london','phone':'12345678'}
user = input("Enter the information wants to know :")
info = data.get(user,'invalid property')
print(info)
