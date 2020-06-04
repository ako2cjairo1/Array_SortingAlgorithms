# (1) Continuously divide the unsorted list until you have N sublists,
# where each sublist has 1 element that is “unsorted”
# and N is the number of elements in the original array.
# (2) Repeatedly merge i.e conquer the sublists together 2 at a time
# to produce new sorted sublists until all elements have been
# fully merged into a single sorted array.

import os
import time
import random as random
import helper


def merge_sort(arr, animate=False):
    # end of array split
    if len(arr) <= 1:
        return arr

    # split the array in half
    mid = len(arr) // 2

    # recursively call the merge_sort to further split the arrays in half
    left, right = merge_sort(
        arr[:mid], animate), merge_sort(arr[mid:], animate)

    # merge each side together
    return merge(left, right, arr.copy(), animate)


def merge(left_arr, right_arr, merged_arr, animate=False):
    steps = 0
    swaps = 0
    # simple representation of bubble sort

    def _show_progress():
        os.system("cls")
        print("")
        print(merged_arr)
        print("Size: ", len(merged_arr))
        print("Current step: ", steps)
        print("Swaps: ", swaps)
        print("")
        # time.sleep(0.1)

    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left_arr) and right_cursor < len(right_arr):

        if left_arr[left_cursor] <= right_arr[right_cursor]:
            merged_arr[left_cursor+right_cursor] = left_arr[left_cursor]
            left_cursor += 1
        else:
            merged_arr[left_cursor+right_cursor] = right_arr[right_cursor]
            right_cursor += 1

        steps += 1
        swaps = steps

        if animate:
            _show_progress()

    # merge the last 2 arrays
    for i in range(left_cursor, len(left_arr)):
        merged_arr[i+right_cursor] = left_arr[i]
        steps += 1
        swaps = steps
        if animate:
            _show_progress()

    for i in range(right_cursor, len(right_arr)):
        merged_arr[left_cursor+i] = right_arr[i]
        steps += 1
        swaps = steps
        if animate:
            _show_progress()

    return merged_arr
