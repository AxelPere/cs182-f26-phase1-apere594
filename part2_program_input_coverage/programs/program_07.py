import sys

if len(sys.argv) < 2:
    result = -1
else:
    collection = [int(x) for x in sys.argv[1:]]

    length = len(collection)
    while True:
        swapped = False
        for i in range(length - 1):
            if collection[i] > collection[i + 1]:
                collection[i], collection[i + 1] = collection[i + 1], collection[i]
                swapped = True
        if not swapped:
            break

    result = collection
