"""
Sum square difference

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def sum_sq_diff(val):
   return sq_sum(val) - sum_sq(val)

def sum_sq(val):
   sum = 0
   for curr in range(1, val+1):
      sum += curr ** 2
   return sum

def sq_sum(val):
   sum = 0
   for curr in range(1, val+1):
      sum += curr
   return sum**2


assert(sum_sq(10) == 385)
assert(sq_sum(10) == 3025)
assert(sum_sq_diff(10) == 2640)

print(sum_sq_diff(100))
