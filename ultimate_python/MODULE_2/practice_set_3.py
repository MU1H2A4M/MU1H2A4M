input = input("Enter a number ")
try:
    number = float(input)
    print(f"The input as a float is: {number}")
    print(f"The type of the input is: {type(number)}")
except ValueError:
    print("Invalid input! Please enter a valid number.")