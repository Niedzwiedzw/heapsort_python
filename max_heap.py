import timeit
from copy import copy

_d = [15, 41, 28, 3, 24, 19, 45, 46,
      14, 31, 47, 2, 18, 42, 17, 4,
      1, 30, 5, 33, 12, 26, 35, 13,
      6, 9, 7, 27, 22, 0, 48, 10, 25,
      16, 40, 39, 29, 20, 11, 34, 32,
      49, 44, 38, 43, 36, 21, 23, 8, 37, -1]

example_data = copy(_d)

heap_size = len(example_data)


def left(index):
    child_index = 2 * index + 1
    return child_index if child_index < heap_size else None


def right(index):
    child_index = 2 * index + 2
    return child_index if child_index < heap_size else None

print(example_data)


def max_heapify(data, index):
    left_child = left(index)
    right_child = right(index)

    if left_child is not None:
        max_heapify(data, left_child)
        if data[left_child] >= data[index]:
            data[left_child], data[index] = data[index], data[left_child]
            max_heapify(data, left_child)

    if right_child is not None:
        max_heapify(data, right_child)
        if data[right_child] >= data[index]:
            data[right_child], data[index] = data[index], data[right_child]
            max_heapify(data, right_child)


def check_if_heap(data):
    for index in range(len(data)):
        if left(index) is not None and data[left(index)] > data[index]:
            return False
        if right(index) is not None and data[right(index)] > data[index]:
            return False
    return True

# print(check_if_heap(example_data))
#
# max_heapify(example_data, 0)
# print(check_if_heap(example_data))


def heap_sort(data):
    global heap_size
    while heap_size > 0:
        max_heapify(data, 0)
        data[0], data[heap_size - 1] = data[heap_size - 1], data[0]
        heap_size -= 1


# print('input data:', example_data)
#
# heap_sort(example_data)
#
# print(example_data)
print('heapsort version')
print(timeit.timeit('heap_sort(example_data)',
                    number=10000000,
                    setup=('from __main__ import heap_sort;'
                           ' from copy import copy;'
                           'from __main__ import _d;'
                           ' example_data=copy(_d)')))

print('python implementation version:')
print(timeit.timeit('example_data.sort()',

                    number=10000000,

                    setup=('from __main__ import heap_sort;'
                           ' from copy import copy;'
                           'from __main__ import _d;'
                           ' example_data=copy(_d)')))




