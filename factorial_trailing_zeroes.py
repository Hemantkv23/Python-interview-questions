from loguru import logger

def trailing_zeroes(n):
    count = 0
    i = 5
    while n // i > 0:
        count += n // i
        i *= 5
    return count

logger.info(trailing_zeroes(125))