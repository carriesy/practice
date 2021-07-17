import random


class Solution(object):

    def random_partition(self, A, p, q):
        r = random.choice(range(p, q))
        A[r], A[p] = A[p], A[r]
        x = A[p]
        i = p
        for j in range(p + 1, q):
            if A[j] >= x:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[p], A[i] = A[i], A[p]

        return i

    def random_select(self, A, p, q, i):
        r = self.random_partition(A, p, q)
        k = r - p + 1
        if k == i:
            return A[r]
        if i < k:
            return self.random_select(A, p, r, i)
        else:
            return self.random_select(A, r + 1, q, i - k)

    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        p = 0
        q = len(nums)
        i = 3 if len(nums) >= 3 else 1  # 返回第三大的数，如果不存在则返回第一大的数

        return self.random_select(nums, p, q, i)
