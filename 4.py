from queue import PriorityQueue
from collections import defaultdict
n, x, y = map(int, input().split())
pq = PriorityQueue()
corrections = defaultdict(lambda: 0)
for i in range(n):
    pq.put((-int(input()), i))
shift = 0
ans = 0
top, idx = pq.get()
top = -top
while top - (shift - corrections[idx] * y) > 0:
    ans += 1
    top -= x
    shift += y
    corrections[idx] += 1
    if top > 0:
        pq.put((-top, idx))
    if pq.qsize() > 0:
        top, idx = pq.get()
        top = -top
print(ans)