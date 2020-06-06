# On each loop iteration, insertion sort removes one element from the array.
# It then finds the location where that element belongs
# within another sorted array and inserts it there.
# It repeats this process until no input elements remain.

import os
import time
import random as random
import helper


def bubble(arr, sort_order='asc'):
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
        # time.sleep(0.1)

    def swap(idx1, idx2):
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

    # def check_sort_order(idx):
    #     return arr[idx - 1] > arr[idx] if sort_order.lower() in "ascending" else arr[idx - 1] < arr[idx]

    last_sorted_idx = 0
    while True:
        unsorted_idx = len(arr) - last_sorted_idx

        for i in range(1, unsorted_idx):
            steps += 1
            # check order, swap if true
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swaps += 1
                _show_progress()

        last_sorted_idx += 1

        # stop if no more unsorted pairs
        if unsorted_idx == 0:
            break

    return arr


def selection(arr, sort_order='asc'):
    min_idx = 0

    def swap(idx1, idx2):
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

    for i in range(len(arr)):
        min_idx = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        swap(min_idx, i)

    return arr


def insertion(arr, sort_order='asc'):
    cursor = 0

    for i in range(len(arr)):
        curr = arr[i]
        cursor = i
        while cursor > 0 and arr[cursor - 1] > curr:
            arr[cursor] = arr[cursor - 1]
            cursor -= 1

        arr[cursor] = curr

    return arr


def merge_sort(arr, run_size=1):
    if len(arr) <= run_size:
        return arr

    mid = len(arr) // 2

    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    return merge(left, right, arr.copy())


def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for i in range(left_cursor, len(left)):
        merged[i + right_cursor] = left[i]

    for i in range(right_cursor, len(right)):
        merged[left_cursor + i] = right[i]

    return merged


def tim(arr):
    RUN = 32

    if len(arr) <= RUN:
        return insertion(arr)
    else:
        return merge_sort(arr, RUN)

    return arr


# for size in [10, 100, 1000, 10000]:
#     arr = helper.create_unsorted_array(size, size)

#     # print(f"Unsorted: {arr}")
#     # # [7, 6, 5, 10, 6, 5, 8, 8, 6, 4]
#     print("=" * 90)
#     print(f"Sorted:   {sorted(arr)}")
