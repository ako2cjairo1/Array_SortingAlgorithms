import random as rand
from time import time
import helper
import bubble_sort as bubble
import selection_sort as selection
import insertion_sort as insertion
import merge_sort as merge


def bench_mark(n=[10, 100, 1000, 10000]):
    bubble_time = []
    selection_time = []
    insertion_time = []
    merge_time = []

    print("\nBenchmark in progress ...")
    print("\n Size      Merge        Selection    Insertion    Bubble")
    print(80 * "-")

    for i, size in enumerate(n):
        unsorted_array = helper.create_unsorted_array(size, size)
        start_time = time()
        merge.merge_sort(unsorted_array)
        end_time = time()
        merge_time.append(end_time - start_time)
        t_merge = '{:0.6f}'.format(merge_time[i])

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
        col3_spacing = 13 - len(t_merge)
        col4_spacing = 13 - len(t_insertion)
        col5_spacing = 13 - len(t_bubble)
        print(
            f" {size}{col1_spacing * ' '}{t_merge}{col3_spacing * ' '}{t_selection}{col2_spacing * ' '}{t_insertion}{col4_spacing * ' '}{t_bubble}{col5_spacing * ' '}")

    print("\n Done!\n")


bench_mark()
