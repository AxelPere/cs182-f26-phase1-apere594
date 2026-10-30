import sys

if len(sys.argv) != 2:
    result = 0
else:
    input_string = sys.argv[1]

    if not input_string:
        result = 0
    else:
        vowels = "aeiouAEIOU"
        result = sum(1 for char in input_string if char in vowels)