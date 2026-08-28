from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter 
        import heapq
        item = list(Counter(nums).items())
        store = []
        n = len(item)
        for i in range(k):
            heapq.heappush(store, (item[i][1], item[i][0]))
        
        for i in range(k, n):
            heapq.heappush(store, (item[i][1], item[i][0]))
            heapq.heappop(store)

        ans = []
        while store:
            ans.append(heapq.heappop(store)[1])
        return ans
                

