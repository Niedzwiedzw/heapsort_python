from typing import List, Callable


class HeapSorter:
    def __init__(self, data: List, key: Callable, reverse: bool = False) -> None:
        '''

        :param data: list of items you wish to sort
        :param key: function which takes a list element and returns a value by which the list should be sorted
        :param reverse: should the list be sorted in reverse ourder?
        '''
        self._data = data
        self.heap_size = len(self._data)
        self.key = key

        self._heapify = self._min_heapify if reverse else self._max_heapify

    def _left(self, index: int) -> int:
        child_index = 2 * index + 1
        return child_index if child_index < self.heap_size else None

    def _right(self, index: int) -> int:
        child_index = 2 * index + 2
        return child_index if child_index < self.heap_size else None

    def _max_heapify(self, index: int) -> None:
        left_child = self._left(index)
        right_child = self._right(index)

        if left_child is not None:
            self._max_heapify(left_child)
            if self.key(self._data[left_child]) > self.key(self._data[index]):
                self._data[left_child], self._data[index] = self._data[index], self._data[left_child]
                self._max_heapify(left_child)

        if right_child is not None:
            self._max_heapify(right_child)
            if self.key(self._data[right_child]) > self.key(self._data[index]):
                self._data[right_child], self._data[index] = self._data[index], self._data[right_child]
                self._max_heapify(right_child)

    def _min_heapify(self, index: int) -> None:
        left_child = self._left(index)
        right_child = self._right(index)

        if left_child is not None:
            self._min_heapify(left_child)
            if self.key(self._data[left_child]) < self.key(self._data[index]):
                self._data[left_child], self._data[index] = self._data[index], self._data[left_child]
                self._min_heapify(left_child)

        if right_child is not None:
            self._min_heapify(right_child)
            if self.key(self._data[right_child]) < self.key(self._data[index]):
                self._data[right_child], self._data[index] = self._data[index], self._data[right_child]
                self._min_heapify(right_child)

    def _heap_sort(self) -> None:
        while self.heap_size > 0:
            self._heapify(0)
            self._data[0], self._data[self.heap_size - 1] = self._data[self.heap_size - 1], self._data[0]
            self.heap_size -= 1

    @classmethod
    def heap_sort(cls, data: List, key: Callable=lambda x: x, reverse: bool=False) -> None:
        cls(data=data, key=key, reverse=reverse)._heap_sort()
