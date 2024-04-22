from loguru import logger

def gcd(a :int, b :int) -> int:
    while b>0:
        a, b = b, a%b
    return a

def lcm(a :int,b :int) ->int:
    return a*b // gcd(a,b) 

def smallest_multiple(input : int) -> int :
    lcm_all = 1
    for i in range(1, input+1):
        lcm_all = lcm(lcm_all, i)
    return lcm_all

input = 11
logger.info(smallest_multiple(input))

# Write a function smallest_multiple to find the smallest number that is perfectly divisible (i.e. no remainder) by all numbers from 1 to the target number.
# For example, if the target value was 5, we'd return 60, because 60 is evenly divisible by 1, 2, 3, 4, and 5. There is no number smaller than 60 which satisfies this condition.