import random
import sys

# This may come in handy...
from fermat import miller_rabin

# If you use a recursive implementation of `mod_exp` or extended-euclid,
# you recurse once for every bit in the number.
# If your number is more than 1000 bits, you'll exceed python's recursion limit.
# Here we raise the limit so the tests can run without any issue.
# Can you implement `mod_exp` and extended-euclid without recursion?
sys.setrecursionlimit(4000)

# When trying to find a relatively prime e for (p-1) * (q-1)
# use this list of 25 primes
# If none of these work, throw an exception (and let the instructors know!)
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


# Implement this function
def ext_euclid(a: int, b: int) -> tuple[int, int, int]:
    """
    The Extended Euclid algorithm
    Returns x, y , d such that:
    - d = GCD(a, b)
    - ax + by = d

    Note: a must be greater than b
    """
    if(b>a):
        c = a
        a = b
        b = c
    if b == 0:
        return 1, 0, a
    xp, yp, d = ext_euclid(b, a % b)
    return yp, (xp - a//b*yp), d


# Implement this function
def generate_large_prime(bits=512) -> int:
    """
    Generate a random prime number with the specified bit length.
    Use random.getrandbits(bits) to generate a random number of the
     specified bit length.
    """
    while True:
        x: int = random.getrandbits(bits)
        if miller_rabin(x, 20) == "prime":
            return x

    


# Implement this function
def generate_key_pairs(bits: int) -> tuple[int, int, int]:
    """
    Generate RSA public and private key pairs.
    Return N, e, d
    - N must be the product of two random prime numbers p and q
    - e and d must be multiplicative inverses mod (p-1)(q-1)
    """
    p: int = generate_large_prime()
    q: int = generate_large_prime()
    N = p*q
    p1q1 = (p-1)*(q-1)
    e = -1
    for i in primes:
        if ext_euclid(p1q1, i)[2] == 1:
            e = i
            break
    if e == -1:
        raise Exception("None of the primes worked for e!")    
    d:int = ext_euclid(p1q1, e)[1]
    if(d<1):
        d += p1q1
        
    return N, e, d

N, e, d = generate_key_pairs(128)
print(f"Here are some keypairs for you for 128 bits!\n\n N:{N}\n\ne:{e}\n\nd:{d}")