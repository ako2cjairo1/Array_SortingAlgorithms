# On each loop iteration, insertion sort removes one element from the array.
# It then finds the location where that element belongs
# within another sorted array and inserts it there.
# It repeats this process until no input elements remain.

import os
import time
import random as random
import helper

# tuple result: (1)sorted array (2)steps made (3)swaps made


def insertion_sort(arr, animate=False):
    min_idx = 0
    swaps = 0
    steps = 0

    # simple representation of bubble sort
    def _show_progress():
        os.system("cls")
        print("")
        print(arr)
        print("Size: ", len(arr))
        print("Current step: ", steps)
        print("Swaps: ", swaps)
        print("")
        time.sleep(0.1)

    def swap(idx1, idx2):
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

    for i in range(len(arr)):
        current = arr[i]
        pos = i

        while pos > 0 and arr[pos - 1] > current:
            swaps += 1
            steps = swaps
            swap(pos, pos - 1)
            if animate:
                _show_progress()
            pos -= 1

        arr[pos] = current
        if animate:
            _show_progress()

    return arr, steps, swaps
