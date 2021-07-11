#!/usr/bin/python

# 快排
def partition(arr, p, q):
    x = arr[p]
    i = p
    for j in range(p + 1, q):
        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i], arr[p] = arr[p], arr[i]
    return i  # 返回主元的索引


def sort(arr, p, q):
    if p < q:
        r = partition(arr, p, q)
        sort(arr, p, r)
        sort(arr, r + 1, q)

    return arr


if __name__ == '__main__':
    a = [6, 10, 13, 5, 8, 3, 2, 11, 123, 45, 61, 24, 79, 86, 45, 34, 32, 67, 7, 8, 2, 90]
    print(sort(a, 0, len(a)))
