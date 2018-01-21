from unittest import TestCase, main
from random import randint
from heap_sorter import HeapSorter

from timeit import timeit


class TestHeapSortCorrectness(TestCase):
    def generate_test_list_data(self):
        self.data = [randint(0, 9999) for _ in range(500)]

    def is_sorted(self, data, reverse=False):
        return all(data[i] <= data[i+1] for i in range(len(data)-1)) if not reverse \
            else all(data[i] >= data[i+1] for i in range(len(data)-1))

    def setUp(self):
        self.generate_test_list_data()

    def test_algorithm_is_correct_for_random_list_data(self):
        for i in range(10):
            HeapSorter.heap_sort(self.data)
            self.assertTrue(self.is_sorted(self.data))
            self.generate_test_list_data()

    def test_algorithm_is_correct_for_random_list_data_reverse_sorted(self):
        for i in range(10):
            HeapSorter.heap_sort(self.data, reverse=True)
            self.assertTrue(self.is_sorted(self.data, reverse=True))
            self.generate_test_list_data()


def bubble_sort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


if __name__ == '__main__':
    main()
    setup = ('from heap_sorter import HeapSorter;'
             'from random import randint;'
             'data = [randint(0, 90) for _ in range(1000)];'
             'from __main__ import bubble_sort')

    print('#####Time comparison')
    print('### my implementation:')
    print(timeit('HeapSorter.heap_sort(data)',
                 setup=setup,
                 number=10))
    print('### bubble sort:')
    print(timeit('bubble_sort(data)',
                 setup=setup,
                 number=10))

    import cProfile

    cProfile.run('HeapSorter.heap_sort([5,2,11,45,6456,3,646,2,3,23,4,41,412,4,24,515,12])')
