import random

def Odd(nums):
    odd_num=[]
    for num in nums:
        if (len(str(num))==3 or len(str(num))==4) and num%2 !=0:
            odd_num.append(num)

    return odd_num

nums = [random.randint(1,1000) for _ in range(20)]

odd_num = Odd(nums)
print(odd_num)