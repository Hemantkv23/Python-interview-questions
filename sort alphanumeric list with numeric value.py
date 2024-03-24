import re

def sort_list(lst):
    l = []
    c= ""
    for i in lst:
        c = ""
        for j in i:
            if j.isdigit():
                c +=j
        l.append((int(c), i))
        l.sort(key=lambda x:x[0])
    return [i[1] for i in l]

def sort_list1(lst):
    l=[]
    for i in lst:
         l.append((int((re.search(r'[0-9]*$', i).group())),i))
    l.sort(key=lambda x:x[0])
    return list(map(lambda x:x[1],l))

lst = ['Sam200','Monu100','Zaid30','Mukesh50','Nisha99']
print(sort_list(lst))
print(sort_list1(lst))