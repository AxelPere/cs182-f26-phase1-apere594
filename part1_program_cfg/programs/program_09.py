import sys
from random import randrange

if len(sys.argv) < 2:
    result = -1
else:
    collection = [int(x) for x in sys.argv[1:]]

    if len(collection) < 2:
        result = collection
    else:
        stack = [(0, len(collection) - 1)]

        while stack:
            low, high = stack.pop()
            if low < high:
                pivot_index = randrange(low, high + 1)
                collection[pivot_index], collection[high] = collection[high], collection[pivot_index]
                pivot = collection[high]

                i = low - 1
                for j in range(low, high):
                    if collection[j] <= pivot:
                        i += 1
                        collection[i], collection[j] = collection[j], collection[i]
                collection[i + 1], collection[high] = collection[high], collection[i + 1]
                pivot_final = i + 1

                stack.append((low, pivot_final - 1))
                stack.append((pivot_final + 1, high))

        result = collection