
# Cache a few primes to get the algorithm started.
# Note: the odd values allow the step of 2 in next_prime()
primes = [2, 3, 5]


def factor_primes(val):
    assert(val > 1)
    factors = []
    remainder = val
    prime_idx = 0
    while remainder > 1 and remainder not in primes:

        # Check if the current remainder is divisible by existing list of primes
        if remainder % primes[prime_idx] == 0:

            # If so, add it to the factorization list, reduce the value
            # to continue searching on
            factors.append(primes[prime_idx])
            remainder = remainder // primes[prime_idx]

        else:
            # Advance to the next highest prime
            prime_idx += 1

            # If we've tested our last known prime, generate the next one
            if prime_idx >= len(primes):
                primes.append(next_prime(primes[-1]))

    # At this point the remainder should be a prime
    # Add it into the factorization list
    assert(remainder in primes)
    factors.append(remainder)

    return factors


def next_prime(curr_prime):

    test_val = curr_prime

    while True:
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
            return test_val


assert factor_primes(2) == [2]
assert factor_primes(3) == [3]
assert factor_primes(5) == [5]
assert factor_primes(7) == [7]
assert factor_primes(8) == [2, 2, 2]
assert factor_primes(13195) == [5, 7, 13, 29]

test_val = 600851475143
test_factors = factor_primes(test_val)
print('Value {} factors into primes: {}'.format(test_val, test_factors))
