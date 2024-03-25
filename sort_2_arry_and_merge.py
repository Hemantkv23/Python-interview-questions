def func(arr1, arr2):
    for i in range(0,len(arr1)):
        for j in range(0,len(arr1)-1):
            if arr1[j+1]>arr1[j]:
                arr1[j],arr1[j+1]=arr1[j+1],arr1[j]
    print(arr1)

    for i in range(0,len(arr2)):
        for j in range(0,len(arr2)-1):
            if arr2[j+1]>arr2[j]:
                arr2[j],arr2[j+1]=arr2[j+1],arr2[j]
    print(arr2)

    merged = []
    i = j = 0

    while(i<len(arr1) and j<len(arr2)):
        if(arr1[i] >= arr2[j]):
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    

    while(i<len(arr1)):
        merged.append(arr1[i])
        i +=1
    while(j<len(arr2)):
        merged.append(arr2[j])
        j +=1
    return merged

arr1 = [7,5,1,10,9]
arr2 = [3,8,2,6,4]

print(func(arr1,arr2))