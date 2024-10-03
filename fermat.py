import argparse
import random


# This is a convenience function for main(). You don't need to touch it.
def prime_test(N: int, k: int) -> tuple[str, str]:
    return fermat(N, k), miller_rabin(N, k)


def mod_exp(x: int, y: int, N: int) -> int:
    if y == 0:
        return 1
    z: int = mod_exp(x, y // 2, N)
    if (y % 2) == 0:
        return (z**2) % N
    else:
        return (x * z**2) % N


# You will need to implement this function and change the return value.
def fprobability(k: int) -> float:
    return (1-1/(2**k))*100


# You will need to implement this function and change the return value.
def mprobability(k: int) -> float:
    return (1-1/(4**k))*100


# You will need to implement this function and change the return value, which should be
# either 'prime' or 'composite'.
#
# To generate random values for a, you will most likely want to use
# random.randint(low, hi) which gives a random integer between low and
# hi, inclusive.
def fermat(N: int, k: int) -> str:
    for _ in range(k):
        a: int = random.randint(1, N-1)
        if(mod_exp(a, N-1, N)) != 1:
            return "composite"
    return "prime"


# You will need to implement this function and change the return value, which should be
# either 'prime' or 'composite'.
#
# To generate random values for a, you will most likely want to use
# random.randint(low, hi) which gives a random integer between low and
# hi, inclusive.
def miller_rabin(N: int, k: int) -> str:
    for _ in range(k):
        d = N-1
        a: int = random.randint(1, d)
        if mod_exp(a, d, N) != 1:
            return "composite"
        while True:
            d //= 2
            if(d%2!=0):
                break
            y = mod_exp(a, d, N)
            if y == -1 or y == N-1:
                break
            elif y != 1:
                return "composite"
    return "prime"


def main(number: int, k: int):
    fermat_call, miller_rabin_call = prime_test(number, k)
    fermat_prob = fprobability(k)
    mr_prob = mprobability(k)

    print(f'Is {number} prime?')
    print(f'Fermat: {fermat_call} (prob={fermat_prob})')
    print(f'Miller-Rabin: {miller_rabin_call} (prob={mr_prob})')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('number', type=int)
    parser.add_argument('k', type=int)
    args = parser.parse_args()
    main(args.number, args.k)
