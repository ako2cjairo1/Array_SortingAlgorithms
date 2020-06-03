# In Selection Sort we first find the smallest element in the unsorted sublist
# and place it at the end of the sorted sublist.
# Thus, we are continuously grabbing the smallest unsorted element
# and placing it in sorted order in the sorted sublist.
# This process continues iteratively until the list is fully sorted.

import os
import time
import random as random
import helper

# tuple result: (1)sorted array (2)steps made (3)swaps made


def selection_sort(arr, animate=False):
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

    for sorted_idx in range(len(arr)):
        # use the last sorted index
        min_idx = sorted_idx

        for unsorted_idx in range(sorted_idx + 1, len(arr)):
            steps += 1
            # update the min_index if there is a smaller than current
            if arr[unsorted_idx] < arr[min_idx]:
                min_idx = unsorted_idx

        # swap the new least number to the sorted list
        swap(min_idx, sorted_idx)
        swaps += 1
        if animate:
            _show_progress()

    return arr, steps, swaps
