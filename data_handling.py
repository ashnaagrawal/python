data_valid = False

while data_valid == False:
    grade1 = float(input("Type the grade of first test:"))
    if grade1 <0 or grade1 > 10 :
        print("Grade should be between 0 and 10")
        continue
    else:
        data_valid = True

data_valid = False
while data_valid == False:
    grade2 = float(input("Type the grade of second test:"))
    if grade2 <0 or grade2 > 10 :
        print("Grade should be between 0 and 10")
        continue
    else:
        data_valid = True

data_valid = False
while data_valid == False:
    total_classes = int(input("Type the total number of classes:"))
    if total_classes <=0:
        print("No. of classes can't be 0")
        continue
    else:
        data_valid = True


data_valid = False
while data_valid == False:
    absences = int(input("Type the number of absences:"))
    if absences <0 or absences > total_classes:
        print("No. of absences can't be less than 0 or greater than the no. of total classes.")
        continue
    else:
        data_valid = True


avg_grade = (grade1 + grade2 )/2
attendance = (total_classes - absences)/total_classes

print("Average grade :" , round(avg_grade))
print("Attendance rate :", str(round((attendance* 100),2)) + "%")

if (avg_grade >=6 and attendance >= 0.8):
    print("The student has been approved")
elif (avg_grade < 6 and attendance < 0.8):
    print("The student has failes due to an average grade lower than 80%")
elif (attendance >= 0.8):
    print("The student has failed due to an average grade lower than 60%")
else:
    print("The student has failed due to an average grade lower than 40%")

