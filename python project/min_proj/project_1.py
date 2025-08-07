def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
   return a/b


def calculator_menu():
    while True:
          print("calculator menu")
          print("1. Add")
          print("2. substract")
          print("3. mul")
          print("4. div")
          choice = input("enter your choice from 1 to 5")

          if choice=='5':
              print("invalid options!")
              break
    
     
     
         
          try:
             num_1 = float(input("enter the number 1 "))
             num_2 = float(input("enter the number 2 "))
          except ValueError:
           print("Invalid input! Please enter numeric values.")
          continue
            
    if  choice == '1':
        print("addition of the number is",add(num_1,num_2))
    elif choice == '2':
           print("substraction",sub(num_1,num_2))
    elif choice == '3':
           print("multiplication",mul(num_1,num_2))
    elif choice == '4':
           print("division",div(num_1,num_2))
    else:
        print("invalid choice!")

calculator_menu()