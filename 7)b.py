import numpy as np

row = int(input("Enter num of rows "))
col = int(input("Enter num of col "))

arr= np.zeros((row,col),dtype = int)

for i in range(row):
    for j in range(col):
        arr[i][j] = int(input(f"Enter element ({i},{j}) : "))
    
print("Array is \n",arr)
    
reverse_arr = np.flip(arr) 
print("\n\nReversed Array is \n",reverse_arr)

principal_dig = np.diag(arr)
print("\n\nPrincipal digonal of Array is \n",principal_dig)

ass_arr = np.sort(arr, axis= None)
ass_arr = ass_arr.reshape(arr.shape)
print("\n\nass Array is \n",ass_arr)

diss_arr = np.sort(arr, axis= None)[::-1]
diss_arr = diss_arr.reshape(arr.shape)
print("\n\nass Array is \n",diss_arr)
