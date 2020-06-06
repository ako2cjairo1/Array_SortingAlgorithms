import random as rand
from time import time
import helper
import bubble_sort as bubble
import selection_sort as selection
import insertion_sort as insertion
import merge_sort as merge
import quick_sort as quick
import tim_sort as tim
import sys

iteration = int(sys.argv[1])


def bench_mark(iteration=5, n=[10, 100, 1000, 10000]):
    print("\nBenchmark in progress ...")

    ave_bubble_time = [0.0, 0.0, 0.0, 0.0]
    ave_selection_time = [0.0, 0.0, 0.0, 0.0]
    ave_insertion_time = [0.0, 0.0, 0.0, 0.0]
    ave_merge_time = [0.0, 0.0, 0.0, 0.0]
    ave_quick_time = [0.0, 0.0, 0.0, 0.0]
    ave_tim_time = [0.0, 0.0, 0.0, 0.0]
    ave_python_time = [0.0, 0.0, 0.0, 0.0]

    def _show_average():

        print("\n" + 42 * "=" + " AVERAGE " + 42 * "=")
        print(" Size      Python     Tim        Quick      Merge      Selection  Insertion  Bubble")
        print(93 * "-")

        for i, size in enumerate(n):
            ave_t_py = '{:0.6f}'.format(ave_python_time[i]/iteration)
            ave_t_tim = '{:0.6f}'.format(ave_tim_time[i]/iteration)
            ave_t_quick = '{:0.6f}'.format(ave_quick_time[i]/iteration)
            ave_t_merge = '{:0.6f}'.format(ave_merge_time[i]/iteration)
            ave_t_selection = '{:0.6f}'.format(ave_selection_time[i]/iteration)
            ave_t_insertion = '{:0.6f}'.format(ave_insertion_time[i]/iteration)
            ave_t_bubble = '{:0.6f}'.format(ave_bubble_time[i]/iteration)

            col1_spacing = 10 - len(str(size))
            col8_spacing = 11 - len(ave_t_py)
            col7_spacing = 11 - len(ave_t_tim)
            col6_spacing = 11 - len(ave_t_quick)
            col2_spacing = 11 - len(ave_t_selection)
            col3_spacing = 11 - len(ave_t_merge)
            col4_spacing = 11 - len(ave_t_insertion)
            col5_spacing = 11 - len(ave_t_bubble)

            print(
                f" {size}{col1_spacing * ' '}{ave_t_py}{col8_spacing * ' '}{ave_t_tim}{col7_spacing * ' '}{ave_t_quick}{col6_spacing * ' '}{ave_t_merge}{col3_spacing * ' '}{ave_t_selection}{col2_spacing * ' '}{ave_t_insertion}{col4_spacing * ' '}{ave_t_bubble}{col5_spacing * ' '}")

    for rep in range(iteration):
        bubble_time = []
        selection_time = []
        insertion_time = []
        merge_time = []
        quick_time = []
        tim_time = []
        py_time = []

        print("\n Iteration #", rep + 1)
        print(" Size      Python     Tim        Quick      Merge      Selection  Insertion  Bubble")
        print(93 * "-")

        for i, size in enumerate(n):

            # benchmark section for Bubble Sort
            unsorted_array = helper.create_unsorted_array(size, size)
            start_time = time()
            bubble.bubble_sort(unsorted_array)
            end_time = time()
            bubble_time.append(end_time - start_time)
            t_bubble = '{:0.6f}'.format(bubble_time[i])

            # Benchmark section for Insertion Sort
            unsorted_array = helper.create_unsorted_array(size, size)
            start_time = time()
            insertion.insertion_sort(unsorted_array)
            end_time = time()
            insertion_time.append(end_time - start_time)
            t_insertion = '{:0.6f}'.format(insertion_time[i])

            # Benchmark section for Selection Sort
            unsorted_array = helper.create_unsorted_array(size, size)
            start_time = time()
            selection.selection_sort(unsorted_array)
            end_time = time()
            selection_time.append(end_time - start_time)
            t_selection = '{:0.6f}'.format(selection_time[i])

            # Benchmark section for Merge Sort
            unsorted_array = helper.create_unsorted_array(size, size)
            start_time = time()
            merge.merge_sort(unsorted_array)
            end_time = time()
            merge_time.append(end_time - start_time)
            t_merge = '{:0.6f}'.format(merge_time[i])

            # Benchmark section for Quick Sort
            unsorted_array = helper.create_unsorted_array(size, size)
            start_time = time()
            quick.quick(unsorted_array)
            end_time = time()
            quick_time.append(end_time - start_time)
            t_quick = '{:0.6f}'.format(quick_time[i])

            # Benchmark section for Tim Sort
            unsorted_array = helper.create_unsorted_array(size, size)
            start_time = time()
            tim.tim(unsorted_array)
            end_time = time()
            tim_time.append(end_time - start_time)
            t_tim = '{:0.6f}'.format(tim_time[i])

            # benchmark section for built-in python sort function
            unsorted_array = helper.create_unsorted_array(size, size)
            start_time = time()
            sorted(unsorted_array)
            end_time = time()
            py_time.append(end_time - start_time)
            t_py = '{:0.6f}'.format(py_time[i])

            # calculate spacing of items
            col1_spacing = 10 - len(str(size))
            col8_spacing = 11 - len(t_py)
            col7_spacing = 11 - len(t_tim)
            col6_spacing = 11 - len(t_quick)
            col2_spacing = 11 - len(t_selection)
            col3_spacing = 11 - len(t_merge)
            col4_spacing = 11 - len(t_insertion)
            col5_spacing = 11 - len(t_bubble)

            # sum the total time(s) of each set
            ave_bubble_time[i] += bubble_time[i]
            ave_insertion_time[i] += insertion_time[i]
            ave_selection_time[i] += selection_time[i]
            ave_merge_time[i] += merge_time[i]
            ave_quick_time[i] += quick_time[i]
            ave_tim_time[i] += tim_time[i]

            # display the current iteration set of benchmarks
            print(f" {size}{col1_spacing * ' '}{t_py}{col8_spacing * ' '}{t_tim}{col7_spacing * ' '}{t_quick}{col6_spacing * ' '}{t_merge}{col3_spacing * ' '}{t_selection}{col2_spacing * ' '}{t_insertion}{col4_spacing * ' '}{t_bubble}{col5_spacing * ' '}")

    _show_average()
    print("\n Done!\n")


bench_mark(iteration)
