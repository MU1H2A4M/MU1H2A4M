marks=int(input("enter the marks of the student "))
if (marks>90 and marks<100):
    print("A+ grade")
elif(marks>80 and marks<90):
    print("A grade")
elif(marks>70 and marks<80):
    print("B grade")
elif(marks>60 and marks<70):
    print("c grade")
elif(marks>50 and marks<60):
    print("D grade")
elif(marks<50):
    print("Congratulations! you are fail ")
else:
    print("do some other works")