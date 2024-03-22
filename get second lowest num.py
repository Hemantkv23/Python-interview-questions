def getSecondLowest(l):
    small = min(l)
    large = max(l)
    for i in l:
        if i<large and i != small:
            large = i 
    return (large)

print(getSecondLowest([1,2,3,4,5,-1]))

