def count_chars(str1):
    lst=[]
    c = 1
    for i in range(1,len(str1)):
        
        if str1[i]==str1[i-1]:
            c += 1
        else:
            lst.append(c)
            c=1 
    lst.append(c)
    return lst

def count_chars2(str1):
    dic = {}
    for i in str1 :
        dic[i]=dic.get(i,0)+1
    return dic.values()
        
from ordered_set import OrderedSet
def count_chars3(str1):
    l=[]
    for i in OrderedSet(str1) :
        l.append(str1.count(i))
    return l

str1 = "bbbbcccaad"  #output [4,3,2,1]
print(count_chars(str1))
print(count_chars2(str1))
print(count_chars3(str1))