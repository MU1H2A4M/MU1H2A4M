def greater(n1,n2,n3):
    n1=int(input("enter the number "))
    n2=int(input("enter the number "))
    n3=int(input("enter the number "))
    if(n1>n2 and n1>n3):
        print("number 1 is greatest ")
    elif(n2>n1 and n2>n3):
        print("number 2 is greatest ")
    elif(n3>n1 and n3>n2):
        print("number 3 is greatest ")
    else:
        print("try to compare another numbers ")



greater()


    