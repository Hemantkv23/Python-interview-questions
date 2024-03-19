def count_len(l):
    if not l :
        return 0
    return 1+count_len(l[1:])

print(count_len([1,2,3,4,5]))