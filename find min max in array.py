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
    for i in range(2,size-1):
        if l[i]>lmax:
            lmax = l[i]
        elif l[i]<lmin :
            lmin = l[i]
    return lmax, lmin

l = [9,1,3,4,5,2,0]
logger.info(find_min_max(l))
