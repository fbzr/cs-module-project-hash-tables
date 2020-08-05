# Your code here
import math
import random

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

slowfun_cache = {}
factorial_cache = {}

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    if (x, y) not in slowfun_cache:
        v = math.pow(x, y)
    
        if v not in factorial_cache:
            factorial_cache[v] = math.factorial(v)
    
        v = factorial_cache[v]
        v //= (x + y)
        v %= 982451653
        
        slowfun_cache[(x, y)] = v

    return slowfun_cache[(x, y)]


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
