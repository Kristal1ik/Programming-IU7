from copy import copy, deepcopy

a = [1, []]
b = copy(a)
c = deepcopy(a)

print(a)
print(b)
print(c)

a[1].append(2)

print(a)
print(b)
print(c)
