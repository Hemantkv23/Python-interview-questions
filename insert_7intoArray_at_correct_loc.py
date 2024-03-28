def insert_7(arr1,n):
    index = len(arr1)
    for i in range(len(arr1)):
        if arr1[i]>n:
            index=i
            break
    if index == len(arr1):
        arr1 = arr1[:index] + [n]
    else:
        arr1 = arr1[:index] + [n] + arr1[index:]
    return arr1

input = [3,6,8,12,15]
input2 = [1,3,4,5,6]
input3 = [8,9,10,12]
input4 = [7,8,9,10,12]

print(insert_7(input,7))
print(insert_7(input2,7))
print(insert_7(input3,7))
print(insert_7(input4,7))