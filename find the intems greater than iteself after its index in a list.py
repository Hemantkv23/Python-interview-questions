#find the intems greater than iteself after its index in a python list
def fin(lst):
    result = []
    max_len = 0
    max_l = []
    for i in range(len(lst)):
        l = []
        for j in range(i, len(lst)):
            if lst[i]<lst[j]:
                l.append(lst[j])
        result.append((lst[i],len(l),l))

        # finding the list with the max len plus the first element
        if max_len<len(l):
            max_len=len(l)
            max_l = [lst[i]] + l
    return result, max_len, max_l


input = [99,28,12,55,13,15,76,99]

print(fin(input))

#output 
# 90 0 []
# 28 3 [55,76,99]
# 12 5 [55,13,15,76,99]
# 55 2 [76,99]
# 13 3 [15,76,99]
# 15 2 [76,99]
# 76 1 [99]
# 99 0 []
