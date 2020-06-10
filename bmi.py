print("This program is to claculate the BMI of a person")
height = float(input("Enter your height in METERS :"))
weight = float(input("Enter your weight in KG :"))
bmi = weight/(height**2)
print('your bmi is:',bmi)
if(bmi<=18.5):
    print('you are underweight')
elif(18.5<bmi<=24.9):
    print('your weight is normal')
elif(24.9<bmi<=29.9):
    print('you are over-weight')
else:
    print('Obesity')
