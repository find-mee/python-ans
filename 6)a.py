def binSearch(arr,key):
    s = 0
    e = len(arr) -1
    m = (s+e)//2
    while s<e:
        if key == arr[m]:
            return 1
        elif key< arr[m]:
            e = m-1
        else:
            s = m+1
        m = (s+e)//2
    return -1
        
arr = [1,2,3,45,67,78,90,111]
key = 90

ans = binSearch(arr,key)
if ans==1:
    print("found")
else:
    print("Not found")