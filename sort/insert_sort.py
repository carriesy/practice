#!/usr/bin/python

# 插入排序
def sort(arr):
    for j in range(1, len(arr)):
        i = j - 1
        while i >= 0 and arr[i] > arr[i + 1]:
            arr[i+1], arr[i] = arr[i], arr[i+1]
            i -= 1
    return a


if __name__ == '__main__':
    a = [2, 3, 1, 4, 2, 5, 7, 3, 9, 4, 5]
    print(sort(a))
