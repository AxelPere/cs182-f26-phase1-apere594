import sys

if len(sys.argv) != 2:
    result = -1
else:
    n = int(sys.argv[1])
    while n < 100:
        n += 1
    result = n