import sys

if len(sys.argv) != 2:
    result = 0
else:
    input_str = sys.argv[1]
    total = 0
    for char in input_str:
        if char.isdigit():
            total += int(char)
    result = total