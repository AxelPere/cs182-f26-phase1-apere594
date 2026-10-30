import sys
import math

if len(sys.argv) != 2:
    result = -1
else:
    n = int(sys.argv[1])

    if n <= 0:
        result = -1
    else:
        div = 1
        temp = 1
        while n % 2 == 0:
            temp += 1
            n = int(n / 2)
        div *= temp
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            temp = 1
            while n % i == 0:
                temp += 1
                n = int(n / i)
            div *= temp
        if n > 1:
            div *= 2

        result = div