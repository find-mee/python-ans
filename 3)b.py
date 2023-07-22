def mmax(arr):
    max = arr[0]
    n = len(arr)
    for i in range(1,n):
        if max<arr[i]:
            max = arr[i]
    print(f"max is {max}")

def mmin(arr):
    min = arr[0]
    n = len(arr)
    for i in range(1,n):
        if min>arr[i]:
            min = arr[i]
    print(f"min is {min}")

def max2(arr):
    max = arr[0]
    max2 = arr[0]
    n = len(arr)
    for i in range(1,n):
        if max<arr[i]:
            max2 = max
            max = arr[i]
    print(f"2nd max is {max2}")

arr = [1,2,43,91,657,2,42,676,11]
print(arr)
mmax(arr)
mmin(arr)
max2(arr)