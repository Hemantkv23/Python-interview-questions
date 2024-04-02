from loguru import logger

def check_leap_year(num):
    count = 0
    if(num%400 == 0  & num%100 == 0 ):
        count = 1
    elif num%4==0 & num%4!= 0:
        count =1
    return count == 1

num = 1900
logger.info(check_leap_year(num))
