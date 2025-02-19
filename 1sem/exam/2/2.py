from os import remove

mx = []
mx_n = 0
mx_m = 0
route_main = []


def find_route(i_main, j_main):
    route = []
    while True:
        if (i_main, j_main) not in route:
            route.append((i_main, j_main))
        else:
            break
        if mx[i_main][j_main] == ">":
            if j_main != mx_m - 1:
                j_main += 1
            else:
                break
        elif mx[i_main][j_main] == "v":
            if i_main != mx_n - 1:
                i_main += 1
            else:
                break
        elif mx[i_main][j_main] == "<":
            if j_main != 0:
                j_main -= 1
            else:
                break
        elif mx[i_main][j_main] == "^":
            if i_main != 0:
                i_main -= 1
            else:
                break
        else:
            break
    return route


with open("in.txt", encoding="utf-8") as f:
    for i in f:
        mx.append(i.split())
        mx_n += 1
        mx_m = len(i.split())

for i in range(mx_n):
    for j in range(mx_m):
        route_now = find_route(i, j)
        if len(route_now) > len(route_main):
            route_main = route_now

counter_columns = [0] * mx_m
for i in route_main:
    counter_columns[i[1]] += 1

mx.append(counter_columns)

pairs = []
for i in range(mx_m):
    pairs.append([counter_columns[i], i])

sorted_pairs = sorted(pairs, key=lambda x: x[0], reverse=True)

sorted_mx = []
for row in mx:
    sorted_row = [row[index] for count, index in sorted_pairs]
    sorted_mx.append(sorted_row)

with open("out.txt", "w", encoding="utf-8") as f:
    for i in range(mx_n + 1):
        for j in range(mx_m):
            f.write(str(sorted_mx[i][j]) + " ")
        f.write("\n")
