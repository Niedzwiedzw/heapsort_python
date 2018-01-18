from unittest import TestCase, main
from random import randint
from heap_sorter import HeapSorter


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

if __name__ == '__main__':
    main()
