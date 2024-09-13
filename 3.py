n = int(input())
list_a = list(map(int, input().split()))
abs_a = [list_a[0]]
for i in range(1, len(list_a)):
    abs_a.append(list_a[i] + abs_a[i-1])


def plus():
    energy = 0
    shift = 0
    for i in range(len(abs_a)):
        corr = abs_a[i] + shift
        if i % 2 == 0:
            if corr <= 0:
                energy += 1 - corr
                shift += 1 - corr
        else:
            if corr >= 0:
                energy += corr + 1
                shift -= corr + 1
    return energy


def minus():
    energy = 0
    shift = 0
    for i in range(len(abs_a)):
        corr = abs_a[i] + shift
        if i % 2 != 0:
            if corr <= 0:
                energy += 1 - corr
                shift += 1 - corr
        else:
            if corr >= 0:
                energy += corr + 1
                shift -= corr + 1
    return energy


print(min(plus(), minus()))
