from random import random
from time import time, sleep

def get_random(lo=0, hi=1):
    start = time()
    sleep(lo + random() * (hi - lo))
    return time() - start
