# Write a python program to create a tuple and perform the following operations   
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)
print()
# •	Adding an items
item = input("Enter an item to enter ")
my_tuple = my_tuple + (item,)
print(my_tuple)
print()
# •	Displaying the length of the tuple
length = len(my_tuple)
print("Lenght of tupple ", length)
print()
# •	Checking for an item in the tuple
item = input("Enter an item to search ")
if item in my_tuple:
    print("Item found")
else:
    print("Not found")
print()
# •	Accessing an items
ind = int(input("Enter an index to search "))
if ind>=0 and ind< length:
    print(f"Item is {my_tuple[ind]}")
else:
    print("index out of bond")