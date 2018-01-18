from heap_sorter import HeapSorter

from json import loads, dumps

with open('./data/randomposts.json', 'r') as f:
    posts = loads(f.read())

for key in posts[0].keys():
    HeapSorter.heap_sort(posts, key=lambda x: x[key])

    with open('./_randomposts_sorted_by_{}.json'.format(key), 'w') as f:
        f.write(dumps(posts, indent=4))
