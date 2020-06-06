import random
import os
import time
import helper


# def qsort(xs):
#     def _show_progress():
#         # os.system("cls")
#         print("")
#         print(xs)
#         print("")
#         # time.sleep(1)

#     if not xs:
#         return xs  # empty sequence case
#     pivot = xs[random.choice(range(0, len(xs)))]
#     # print(pivot)
#     head = qsort([x for x in xs if x < pivot])
#     tail = qsort([x for x in xs if x > pivot])
#     # _show_progress()
#     return head + [x for x in xs if x == pivot] + tail

def quick(arr):
    if len(arr) < 2:
        return arr

    def swap(idx1, idx2):
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

    def partition(arr, begin_idx, end_idx):
        pivot_idx = begin_idx
        for i in range(begin_idx + 1, end_idx + 1):
            if arr[i] < arr[begin_idx]:
                pivot_idx += 1
                swap(i, pivot_idx)
        swap(pivot_idx, begin_idx)

        return pivot_idx

    def quick_sort(arr, begin_idx, end_idx):
        if begin_idx >= end_idx:
            return

        pivot_idx = partition(arr, begin_idx, end_idx)
        quick_sort(arr, begin_idx, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, end_idx)

    quick_sort(arr, 0, len(arr) - 1)
    return arr
