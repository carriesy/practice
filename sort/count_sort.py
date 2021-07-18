
def counting_sort(a):
    k = max(a)
    c = [0] * (k + 1)  # 初始化存储序列
    for i in range(len(a)):
        c[a[i]] = c[a[i]] + 1  # 对每个元素进行计频,元素的值为c中的索引

    for j in range(1, k + 1):
        c[j] = c[j] + c[j - 1]  # 对c的元素进行累加

    b = [0] * len(a)
    for j in range(len(a) - 1, -1, -1):
        b[c[a[j]] - 1] = a[j]  # c的值即为元素在b中的索引
        c[a[j]] = c[a[j]] - 1
    return b


if __name__ == '__main__':

    a = [4, 3, 4, 6, 1, 2]
    print(counting_sort(a))
