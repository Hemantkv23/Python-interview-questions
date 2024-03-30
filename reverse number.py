from loguru import logger

def reverse_num(num: int)-> int:
    nstr = list(str(num))
    i = 0
    j = len(nstr)-1
    while(i <= j):
        nstr[i], nstr[j] = nstr[j], nstr[i]
        i +=1
        j -=1
    return ''.join(nstr)

logger.info(reverse_num(1234))