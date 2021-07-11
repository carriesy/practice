#!/usr/bin/python

# 归并排序
def merge(left, right):
    temp = []
    i = 0
    j = 0
    n = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            temp.append(left[i])
            i = i + 1
            n += 1
        else:
            temp.append(right[j])
            j = j + 1
            n += 1

    if i < len(left):
        temp[n:] = left[i:]

    if j < len(right):
        temp[n:] = right[j:]

    return temp


def sort(arr):
    if len(arr) >= 2:
        middle = int(len(arr) / 2)
        left = arr[0:middle]
        right = arr[middle:]
        print(left, right)
        return merge(sort(left), sort(right))
    else:
        return arr


if __name__ == '__main__':
    a = [1, 31, 50, 21, 31, 42, 54, 67, 34]
    print(sort(a))
