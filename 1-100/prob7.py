"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?

https://projecteuler.net/problem=7
"""

# Cache a few primes to get the algorithm started.
# Note: the odd values allow the step of 2 in next_prime()
primes = [2, 3, 5]

# Shortcut for multi-use: save the largest non-prime
# tested for subsequent prime searches
# test_val = primes[-1]


def prime_number(count):
    """
    Returns the nth prime.
    Adapted from code in prob3.py
    """
    test_val = primes[-1]
    while len(primes) <= count:
        # No point testing even numbers
        test_val += 2

        divisible = False

        # Compare to known primes
        for i in primes:
            if test_val % i == 0:
                divisible = True
                break

        if not divisible:
            # New prime found!
            primes.append(test_val)

    # print(primes, count, primes[count - 1])
    result = primes[count - 1]
    # print("Prime #{} is {}".format(count, result))
    return primes[count - 1]

assert prime_number(1) == 2
assert prime_number(2) == 3
assert prime_number(3) == 5
assert prime_number(4) == 7
assert prime_number(5) == 11
assert prime_number(6) == 13
print(prime_number(10001))
