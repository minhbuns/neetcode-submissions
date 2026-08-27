class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import defaultdict
        Hmap = defaultdict(int)
        for i in nums:
            Hmap[i] += 1
            if Hmap[i] > 1:
                return True
        return False