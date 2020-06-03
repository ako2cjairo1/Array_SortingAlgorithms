# Bubble sort steps through the list and compares adjacent pairs of elements.
# The elements are swapped if they are in the wrong order.
# The pass through the unsorted portion of the list is repeated
# until the list is sorted.

import os
import random as rand
import time

# tuple result: (1)sorted array (2)steps made (3)swaps made


def bubble_sort(arr, show_animation=False):
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

    # helper function swapping 2 numbers in array
    def _swap(idx1, idx2):
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

    swaped = True
    last_sorted_idx = -1

    while swaped:
        swaped = False
        last_sorted_idx = last_sorted_idx + 1

        # loop through the length of array
        for curr_index in range(1, len(arr) - last_sorted_idx):
            steps += 1
            # check current adjacent for larger number
            if arr[curr_index - 1] > arr[curr_index]:
                # swap the numbers, put the larger number on the right side
                _swap(curr_index - 1, curr_index)
                swaps += 1
                if show_animation:
                    _show_progress()
                swaped = True

    return arr, steps, swaps
