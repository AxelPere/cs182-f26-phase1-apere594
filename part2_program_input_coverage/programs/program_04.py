import sys
from string import ascii_lowercase, ascii_uppercase

if len(sys.argv) != 2:
    result = ""
else:
    sentence = sys.argv[1]

    if not sentence:
        result = ""
    else:
        lower_to_upper = dict(zip(ascii_lowercase, ascii_uppercase))
        first_char = sentence[0]
        capitalized_first = lower_to_upper.get(first_char, first_char)
        result = capitalized_first + sentence[1:]