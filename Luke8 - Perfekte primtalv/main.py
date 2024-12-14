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

def finn_primtall(n):
    primtall = []
    i=2
    while len(primtall) < n:
        if primes.check(i):
            primtall.append(i)
        i += 1
    return primtall

def primtalv(n):
    primtall = finn_primtall(n)
    siffersummer = {}

    for tall in primtall:
        tallstreng = str(tall)
        for i, siffer in enumerate(tallstreng):
            if str(i) not in siffersummer:
                siffersummer[str(i)] = int(siffer)
            else:
                siffersummer[str(i)] += int(siffer)
    
    for i, siffer in siffersummer.items():
        siffersummer[i] *= 10**int(i)
    
    return sum(siffersummer.values())

@timing_val
def finn_antall_perfekte_primtalv():
    antall_perfekte_primtalv = 0
    n = 0
    while (prim := primtalv(n)) < 10_000_000:
        if primes.check(prim):
            antall_perfekte_primtalv += 1
        n+=1
        print(f"Calculating... {prim/10_000_000*100:.0f}% done", end="\r")
    print("")
    return antall_perfekte_primtalv

print(finn_antall_perfekte_primtalv())