import sys

if len(sys.argv) != 2:
    result = -1
else:
    i = int(sys.argv[1])
    
    i_plus_1 = i + 1

    while True:
        i_plus_1 += 1

    i_minus_1 = i - 1
    result = i_minus_1