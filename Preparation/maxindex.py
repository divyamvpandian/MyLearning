from collections import namedtuple
Entry = namedtuple('Entry', ['value', 'idx'])

arr = {9, 2, 3, 4, 5, 6, 7, 8, 18, 0}
entries = [Entry(v, i) for i, v in enumerate(arr)]
print(entries)
entries.sort(key=lambda x: x.value)
print(entries)
minIdx = len(entries)
maxIJ = 0
for e in entries:
    maxIJ = max(maxIJ, e.idx-minIdx)
    minIdx = min(minIdx, e.idx)
print(maxIJ)