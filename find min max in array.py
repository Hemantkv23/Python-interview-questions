from loguru import logger

def find_min_max(l):
    size = len(l)
    lmax = 0
    lmin = 0
    if size == 1:
        lmax = l[0]
        lmin = l[0]
        return lmax, lmin
    
    if l[0]>l[1]:
        lmax = l[0]
        lmin = l[1]
    else:
        lmin = l[0]
        lmax = l[1]
    for i in range(2,size):
        if l[i]>lmax:
            lmax = l[i]
        elif l[i]<lmin :
            lmin = l[i]
    return lmax, lmin

def find_min_max2(l):
    size = len(l)
    if size % 2 ==0 :
        if l[0]<l[1]:
            lmin=l[0]
            lmax=l[1]
        else:
            lmin = l[1]
            lmax = l[0]
    else:
        lmin = lmax = l[0]

    i = 1

    while(i<size-1):
        if l[i]<l[i+1]:
            lmin = min(lmin, l[i])
            lmax = max(lmax, l[i+1])
        else:
            lmin = min(lmin, l[i+1])
            lmax = max(lmax, l[i])

        i = i+2 #compairing in pairs
    return lmax, lmin
            


l = [9,1,3,4,5,2,0]
logger.info(find_min_max(l))
logger.info(find_min_max2(l))
