def demonstrate_exceptions():
    try:
     # Name Error
        print(undefined_variable)
    except NameError:
        print("Caught a NameError: The variable is not defined.")
    try:
     # Index Error
        my_list = [1, 2, 3]
        print(my_list[5])
    except IndexError:
        print("Caught an IndexError: Index is out of range.")
    try:
     # Key Error
        my_dict = {"key": "value"}
        print(my_dict["nonexistent_key"])
    except KeyError:
        print("Caught a KeyError: The key does not exist in the dictionary.")
    try:
     # Zero Division Error
        result = 10 / 0
    except ZeroDivisionError:
        print("Caught a ZeroDivisionError: Cannot divide by zero.")

demonstrate_exceptions()
