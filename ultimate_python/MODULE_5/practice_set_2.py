number=[]

for i in range(8):
 n=int(input("enter the numbers {i+1} "))
 number.append(n)

 unique_number=set(number)
 print("list of the unique number is ",unique_number)