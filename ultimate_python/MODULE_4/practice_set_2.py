# Create a tuple
my_tuple = (1, 2, 3, 4, 5)

# Try to change an element in the tuple
try:
    my_tuple[0] = 10  # Attempt to modify the first element
except TypeError as e:
    print("Error:", e)

# Try to add an element to the tuple
try:
    my_tuple += (6,)  # Attempt to add a new element
except TypeError as e:
    print("Error:", e)
else:
    print("New tuple after adding an element:", my_tuple)