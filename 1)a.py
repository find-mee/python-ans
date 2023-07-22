num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))

print("\n1.Add\n2.Sub\n3.Multi\4.Divide\n")
ch = int(input("Enter a choice "))

if ch ==1:
    print(num1 + num2)
elif ch ==2:
    print(num1 - num2)
elif ch ==3:
    print(num1 * num2)
elif ch ==4:
    print(num1 / num2)
else:
    print("invalid choice")