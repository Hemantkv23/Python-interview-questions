def count_frequency(l):
    dic = dict()
    for i in l:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    return dic


def count_frequency1(l):
    dic = dict()
    for i in l:
        dic[i]=dic.get(i,0)+1
    return dic

print(count_frequency([1,1,2,2,3,4,4,4,4,5,5,5,5]))
print(count_frequency1([1,1,2,2,3,4,4,4,4,5,5,5,5]))