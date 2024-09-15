from collections import defaultdict
n, m, k = map(int, input().split())
lst = []
d = defaultdict(lambda: 0)
for i in range(k):
    s = input()
    d[s] = 1
    lst.append(list(map(int, s.split())))


ans = [0 for i in range(10)]
for i in range(k):
    count = 0
    for x in range(lst[i][0] - 1, lst[i][0] + 2):
        for y in range(lst[i][1] - 1, lst[i][1] + 2):
            count += d[str(x) + " " + str(y)]
    ans[count] += 1
ans[0] = (n - 2) * (m - 2) - sum(ans)
print(*ans, sep='\n')


