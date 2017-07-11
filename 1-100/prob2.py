# Setting to True clearly shows the neat Fibonacci pattern of:
# Odd, Odd, Even, O, O, E, O, O, E....
DEBUG = False

total = 0
curr = 1
prev = 1
while curr < 4000000:
    if curr % 2 == 0:
        if DEBUG:
            print('adding   {}'.format(curr))
        total += curr
    else:
        if DEBUG:
            print('skipping {}'.format(curr))

    # I love this old-school trick. No risk of overflows at just 8 million.
    curr = prev + curr
    prev = curr - prev

print(total)
