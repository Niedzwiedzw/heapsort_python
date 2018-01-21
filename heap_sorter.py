from typing import List, Callable


class HeapSorter:
    def __init__(self, data: List, key: Callable, reverse: bool = False) -> None:
        '''

        :param data: list of items you wish to sort
        :param key: function which takes an element and returns a value by which the list should be sorted by
        :param reverse: should the list be sorted in reverse ourder?
        '''
        self._data = data
        self._key = key

        self._heapify = getattr(self, '{}_heapify{}'.format('_min' if reverse else '_max',
                                                            '_keyed' if key is not None else ''))

    def _max_heapify(self, heap_size, index):
        data = self._data
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < heap_size and data[index] < data[left]:
            largest = left

        if right < heap_size and data[largest] < data[right]:
            largest = right

        if largest != index:
            data[index], data[largest] = data[largest], data[index]  # swap

            self._heapify(heap_size, largest)

    def _min_heapify(self, heap_size, index):
        data = self._data
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < heap_size and data[index] > data[left]:
            largest = left

        if right < heap_size and data[largest] > data[right]:
            largest = right

        if largest != index:
            data[index], data[largest] = data[largest], data[index]  # swap

            self._heapify(heap_size, largest)

    def _max_heapify_keyed(self, heap_size, index):
        data = self._data
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < heap_size and self._key(data[index]) < self._key(data[left]):
            largest = left

        if right < heap_size and self._key(data[largest]) < self._key(data[right]):
            largest = right

        if largest != index:
            data[index], data[largest] = data[largest], data[index]  # swap

            self._heapify(heap_size, largest)

    def _min_heapify_keyed(self, heap_size, index):
        data = self._data
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < heap_size and self._key(data[index]) > self._key(data[left]):
            largest = left

        if right < heap_size and self._key(data[largest]) > self._key(data[right]):
            largest = right

        if largest != index:
            data[index], data[largest] = data[largest], data[index]  # swap

            self._heapify(heap_size, largest)

    def _heap_sort(self):
        data = self._data
        heap_size = len(data)

        for index in range(heap_size, -1, -1):
            self._heapify(heap_size, index)

        for index in range(heap_size - 1, 0, -1):
            data[index], data[0] = data[0], data[index]  # swap
            self._heapify(index, 0)

    @classmethod
    def heap_sort(cls, data: List, key: Callable or None=None, reverse: bool=False) -> None:
        cls(data=data, key=key, reverse=reverse)._heap_sort()
