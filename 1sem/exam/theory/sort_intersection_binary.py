def insertion_binary(data):
    for i in range(len(data)):
        key = data[i]
        lo, hi = 0, i - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if key < data[mid]:
                hi = mid
            else:
                lo = mid + 1
        for j in range(i, lo + 1, -1):
            data[j] = data[j - 1]
        data[lo] = key
    return data
