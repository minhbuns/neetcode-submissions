from typing import List 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [nums[0]]
        suf = [nums[-1]]
        n = len(nums)
        for i in nums[1::]:
            pre.append(pre[-1] * i)
        for i in range(n - 2, -1, -1):
            suf.append(suf[-1] * nums[i])
        ans = []
        suf = suf[::-1]
        for i in range(n):
            a = 1 if i == 0 else pre[i - 1]
            b = 1 if i == n - 1 else suf[i + 1]
            ans.append(a * b)
        return ans
