example_data = [15, 41, 28, 3, 24, 19, 45, 46,
                14, 31, 47, 2, 18, 42, 17, 4,
                1, 30, 5, 33, 12, 26, 35, 13,
                6, 9, 7, 27, 22, 0, 48, 10, 25,
                16, 40, 39, 29, 20, 11, 34, 32,
                49, 44, 38, 43, 36, 21, 23, 8, 37]

max = len(example_data) - 1


def left(index):
    child_index = 2 * index + 1
    return child_index if child_index < max else None


def right(index):
    child_index = 2 * index + 2
    return child_index if child_index < max else None

print(example_data)


def max_heapify(data, index):
    left_child = left(index)
    right_child = right(index)

    if left_child is not None:
        max_heapify(data, left_child)
        if data[left_child] > data[index]:
            data[left_child], data[index] = data[index], data[left_child]
            max_heapify(data, index)

    if right_child is not None:
        max_heapify(data, right_child)
        if data[right_child] > data[index]:
            data[right_child], data[index] = data[index], data[right_child]
            max_heapify(data, index)



def check_if_heap(data):
    for index in range(len(data)):
        print(index, ' left:', data[index] > data[left(index)] if left(index) is not None else 'end')
        print(index, ' right:', data[index] > data[right(index)] if right(index) is not None else 'end')
        print()

max_heapify(example_data, 0)
print(example_data)
check_if_heap(example_data)

