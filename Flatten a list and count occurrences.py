def flatten_list(lst):
    dic = {}
    l = []
    for i in lst:
        if (isinstance(i,list)):
            for j in i:
                dic[j] = dic.get(j,0) +1
                l.append(j)
    return dic,l

def flatten_list1(lst):
    dic = {}
    l = []
    for i in lst:
        l.extend(i)
    for i in l:
        dic[i] = dic.get(i,0) +1
    return dic, l

from itertools import chain
def flatten_list2(lst):
    dic = {}
    for i in list(chain.from_iterable(lst)):
        dic[i] = dic.get(i,0)+1
    return dic

input_list=[[1,2],[3,4],[2,3],[5,1],[7,1,2]]
print(flatten_list(input_list))
print(flatten_list1(input_list))
print(flatten_list2(input_list))
#output={1:3,2:3,3:2,4:1,5:1,7:1}