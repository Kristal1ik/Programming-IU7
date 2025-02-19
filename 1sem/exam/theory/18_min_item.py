lst = [9, 1, 2, 5, 4]
min_item = lst[0]
min_index = 0
for i, item in enumerate(lst):
    if item < min_item:
        min_index, min_item = i, item
print("Min item is list[{}] = {}".format(min_index, min_item))
