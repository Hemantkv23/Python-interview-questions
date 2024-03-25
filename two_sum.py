def two_sum(lst, target):
    result = []
    for i in range(0, len(lst)):
        for j in range(i+1,len(lst)):
            if(lst[i] + lst[j]==target):
                result.append((i,j))
    return result

l = [2,7,11,15,7,0,8,9,1]
target = 9
print(two_sum(l,target))
