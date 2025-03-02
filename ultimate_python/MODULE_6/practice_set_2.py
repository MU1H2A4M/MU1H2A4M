sub1_marks=int(input("enter the marks of a course "))
sub2_marks=int(input("enter the marks of a course "))
sub3_marks=int(input("enter the marks of a course "))

sum=sub1_marks+sub2_marks+sub3_marks
percentage=((sum)/300)*100
if percentage>40 and sub1_marks>33 and sub2_marks>33 and sub3_marks>33:
    print("Congratulations you have passed the exams!")
else:
    print("You have failed!")