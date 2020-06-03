import random as rand

# helper function that create randomized unsorted numbers.


def create_unsorted_array(size, max_range):
    return [rand.randint(1, max_range) for _ in range(size)]
