import sys
import math

if len(sys.argv) != 2:
    result = -1
else:
    n = int(sys.argv[1])

    if n <= 0:
        result = -1
    else:
        factors = []

        while n % 2 == 0:
            factors.append(2)
            n //= 2

        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                factors.append(i)
                n //= i

        if n > 2:
            factors.append(n)

        result = factors