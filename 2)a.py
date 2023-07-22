num1 = int(input("starting number "))
num2 = int(input("ending number "))

for i in range(num1,num2):
    is_prime=True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            is_prime = False
            break
    if is_prime:
            print(i)


