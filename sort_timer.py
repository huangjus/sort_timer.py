# Author: Justin Huang
# GitHub username: huangjus
# Date: 5/23/23
# Description: This code measures and compares the execution time of bubble sort and insertion sort algorithms. It uses
# a decorator to time the sorting functions and generates a graph to visualize their performance.

import time
import random
from functools import wraps
from matplotlib import pyplot as plt


def sort_timer(func):
    """
    Decorator function to time the decorated function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wrapper function that measures the elapsed time of the decorated function.

            *args: Variable length arguments.
            **kwargs: Keyword arguments.
        """
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        return elapsed_time
    return wrapper


@sort_timer
def bubble_sort(a_list):
    """
    Sorts a_list in ascending order using the bubble sort algorithm.
    """
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp


@sort_timer
def insertion_sort(a_list):
    """
    Sorts a_list in ascending order using the insertion sort algorithm.
    """
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value


def compare_sorts(bubble_sort_func, insertion_sort_func):
    """
    Compare the sorting algorithms by measuring their execution time for different list sizes.
    """
    list_sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    bubble_sort_times = []
    insertion_sort_times = []

    for size in list_sizes:
        data = [random.randint(1, 10000) for _ in range(size)]

        # Measure time for bubble sort
        bubble_sort_time = bubble_sort_func(data)
        bubble_sort_times.append(bubble_sort_time)

        # Measure time for insertion sort
        insertion_sort_time = insertion_sort_func(data)
        insertion_sort_times.append(insertion_sort_time)

    # Generate the graph
    plt.plot(list_sizes, bubble_sort_times, 'ro--', linewidth=2, label='Bubble Sort')
    plt.plot(list_sizes, insertion_sort_times, 'go--', linewidth=2, label='Insertion Sort')
    plt.xlabel("Number of Elements")
    plt.ylabel("Time (seconds)")
    plt.legend(loc='upper left')
    plt.show()


# Call the compare_sorts function to generate the graph
compare_sorts(bubble_sort, insertion_sort)
