from heap_sorter import HeapSorter

from csv import reader, writer


with open('./data/allstars.csv', 'r', newline='') as f:
    data = [row for row in reader(f, delimiter=',')]

for column_number in range(len(data[0])):
    HeapSorter.heap_sort(data, key=lambda x: x[column_number])

    with open('_allstars_sorted_by_column_{}.csv'.format(column_number), 'w') as f:
        w = writer(f)
        w.writerows(data)
