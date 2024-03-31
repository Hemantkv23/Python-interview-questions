from loguru import logger

def fibbonacci_recursion(num):
    if num==1:
        return 0
    elif num == 2 : 
        return 1
    elif num >2 :
        return fibbonacci_recursion(num-1)+fibbonacci_recursion(num-2)

def get_fibonacchi(num):
    fib = []
    for i in range(1, num+1):
        fib.append(fibbonacci_recursion(i))
    return fib

num = 5
logger.info(f'fibonaaci with {num} digits: {get_fibonacchi(num)}')