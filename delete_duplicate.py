from loguru import logger

def delete_duplicate(input:str)->str:
    lst = input.split(' ')
    dic = {}
    for i in lst:
        dic[i] = dic.get(i,0) + 1
    output=' '.join([key for key,value in dic.items() if value == 1])    
    return output

input = "This is a string a with with a few a duplicates"
logger.info(delete_duplicate(input))