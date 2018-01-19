# HeapSort implemented in Python
`by niedzwiedzwo@gmail.com`

I struggled to find an implementation of the algorithm that I would find readable, so here it is.
It uses Python 3.5+ feature `-> type hints`.

## basic usage

```python
from heap_sorter import HeapSorter

some_data = [5, 2, 66, 4]

HeapSorter.heap_sort(some_data)  # watch out, it mutates the original object!

print(some_data)

# out: [2, 4, 5, 66]
 
```

additional parameters are `key` and `reverse`

```python
from heap_sorter import HeapSorter
from collections import namedtuple

ElvisSong = namedtuple('ElvisSong', ['title', 'year', 'album'])

songs = [
    ElvisSong('Jailhouse Rock', 1957, 'Jailhouse Rock'),
    ElvisSong('That\'s All Right', 1956, 'Elvis Presley'),
    ElvisSong('Return to Sender', 1962, 'Girls! Girls! Girls!'),
    ElvisSong('It\'s now or never', 1960, 'Elvis is Back!'),
    
]

HeapSorter.heap_sort(songs, key=lambda song: song.year, reverse=True)

from pprint import pprint  # just for a more readable output
pprint(songs)

# out: [ElvisSong(title='Return to Sender', year=1962, album='Girls! Girls! Girls!'),
#       ElvisSong(title="It's now or never", year=1960, album='Elvis is Back!'),
#       ElvisSong(title='Jailhouse Rock', year=1957, album='Jailhouse Rock'),
#       ElvisSong(title="That's All Right", year=1956, album='Elvis Presley')]
```