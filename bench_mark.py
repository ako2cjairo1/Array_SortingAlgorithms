import random as rand
from time import time
import helper
import bubble_sort as bubble
import selection_sort as selection
import insertion_sort as insertion


def bench_mark(n=[10, 100, 1000, 10000, 100000]):
    bubble_time = []
    selection_time = []
    insertion_time = []

    print("\nBenchmark in progress ...")
    print("\n Size\t   Selection \tInsertion    Bubble")
    print(80 * "-")

    for i, size in enumerate(n):
        unsorted_array = helper.create_unsorted_array(size, size)
        start_time = time()
        selection.selection_sort(unsorted_array)
        end_time = time()
        selection_time.append(end_time - start_time)
        t_selection = '{:0.6f}'.format(selection_time[i])

        unsorted_array = helper.create_unsorted_array(size, size)
        start_time = time()
        insertion.insertion_sort(unsorted_array)
        end_time = time()
        insertion_time.append(end_time - start_time)
        t_insertion = '{:0.6f}'.format(insertion_time[i])

        unsorted_array = helper.create_unsorted_array(size, size)
        start_time = time()
        bubble.bubble_sort(unsorted_array)
        end_time = time()
        bubble_time.append(end_time - start_time)
        t_bubble = '{:0.6f}'.format(bubble_time[i])

        col1_spacing = 10 - len(str(size))
        col2_spacing = 13 - len(t_selection)
        col3_spacing = 13 - len(t_insertion)
        col4_spacing = 14 - len(t_bubble)
        print(
            f" {size}{col1_spacing * ' '}{t_selection}{col2_spacing * ' '}{t_insertion}{col3_spacing * ' '}{t_bubble}{col4_spacing * ' '}")

    print("\n Done!\n")


bench_mark()
