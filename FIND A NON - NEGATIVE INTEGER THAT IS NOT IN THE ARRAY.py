

def miss(l):
    res = []
    for i in range(max(l)):
        if i not in l:
            res.append(i)
    return res

l = [0,1,2,3,4,5] #[]
l1 = [1,2,3,4,5]  #[0]
l2 = [1,2,4,5]    #[0,3]
print(miss(l2))