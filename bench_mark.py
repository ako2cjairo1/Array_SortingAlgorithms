import random as rand
from time import time
import helper
import bubble_sort as bubble
import selection_sort as selection


def bench_mark(n=[10, 100, 1000, 10000]):
    bubble_time = []
    selection_time = []
    insertion_time = []

    print("\nBench marking in progress ...")
    print("\n Size\t\tInsertion\t\tSelection\t\tBubble")
    print(80 * "-")

    for size in n:
        unsorted_array = helper.create_unsorted_array(size, size)
        start_time = time()
        bubble.bubble_sort(unsorted_array)
        end_time = time()
        bubble_time.append(end_time - start_time)

        unsorted_array = helper.create_unsorted_array(size, size)
        start_time = time()
        selection.selection_sort(unsorted_array)
        end_time = time()
        selection_time.append(end_time - start_time)

    for i, size in enumerate(n):
        print(
            f" {size}\t\t{'{:0.5f}'.format(0.00)}\t\t\t{'{:0.5f}'.format(selection_time[i])}\t\t\t{'{:0.5f}'.format(bubble_time[i])}")

    print("\nDone\n")


bench_mark()
