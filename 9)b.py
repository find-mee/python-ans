def divide_numbers(a, b):
    try:
        c = a/b
        print(f"{a}/{b} = {c}")
    except ZeroDivisionError:
        print("Cannot divide by 0")
    except Exception as e:
        print(f"Error occured {str(e)}")
    else:
        print("No error")
    finally:
        print("Finally block")


# Example usage
divide_numbers(10, 2)
divide_numbers(10, 0)
divide_numbers(10, '2')
divide_numbers('10', 2)
