import random
from loguru import logger

num = random.random()
logger.info(f'prints the random float between 0,1: {num}')

num = random.uniform(0,100)
logger.info(f'prints the random float in range(1,100): {num}')

num = random.randint(1,100)
logger.info(f'prints the random integer in range(1,100): {num}')

num = random.randrange(0,100,2)
logger.info(f'prints the random even integer in range(0,100): {num}')

num = random.sample(range(0,100),4)
logger.info(f'prints the range sample of 4 in range(0,100): {num}')