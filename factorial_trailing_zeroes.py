https://datalemur.com/questions/python-factorial-trailing-zeroes

Before, you work on this question, make sure you've solved the easier warmup problem Factorial Formula, where you need to write a function to compute 
n factorial as follows:
n!=n∗(n−1)∗(n−2)∗.....2∗1.
Now that you know the factorial formula, let's write a function that returns the number of trailing zeroes in n!.
For example, for 
5!, we'd return 1, because 
5!=5∗4∗3∗2∗1=120 and 120 has exactly 1 trailing zero.
For 10!, which evaluates to 3628800 we'd return 2, becuase there are two trailing zeroes.

Solution-

1st approch - 

def how_much_5(n):
  if (n%5) != 0 :
    return (0)
  else:
    return (1+ how_much_5(n/5))

def trailing_zeroes(n):
  sum = 0
  while n>=5:
    sum += how_much_5(n)
    n -= 1
  return sum


2nd approch -

from loguru import logger

def trailing_zeroes(n):
    count = 0
    i = 5
    while n // i > 0:
        count += n // i
        i *= 5
    return count

logger.info(trailing_zeroes(125))
