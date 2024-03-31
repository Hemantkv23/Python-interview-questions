from loguru import logger

def get_fibonacci(num: int)-> list:
    fib = []
    a, b = 0, 1
    if num<1:
        return fib
    if num==1:
        fib = [a]
        return fib
    if num==2:
        fib = [a,b]
        return fib
    if num>2:
        fib = [a,b]
        while num>2:
            c = a+b
            fib.append(c)
            a, b = b, c
            num -=1
        return fib
num = 10
logger.info(f'Fibbonacci series upto {num} numbers: {get_fibonacci(num)}')
        

    