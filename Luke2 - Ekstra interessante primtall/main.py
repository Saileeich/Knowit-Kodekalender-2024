from primePy import primes
import time

def timing_val(func):
    def wrapper(*arg, **kw):
        '''source: http://www.daniweb.com/code/snippet368.html'''
        t1 = time.time()
        res = func(*arg, **kw)
        t2 = time.time()
        return (t2 - t1), res, func.__name__
    return wrapper

def tverrsum(num):
    nsum = 0
    for c in str(num):
        nsum += int(c)
    return nsum

@timing_val
def find_special_primes(n):
    prime = []
    spec_prime = []
    i=2
    while len(spec_prime) < n:
        if primes.check(i):
            prime.append(i)
            if (tverrsum(len(prime)) == tverrsum(i)):
                spec_prime.append(i)
        i += 1
    return sum(spec_prime)

print(find_special_primes(10_000))
