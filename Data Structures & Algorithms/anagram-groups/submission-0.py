class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter
        cSet = {}
        for s in strs:
            c = frozenset(Counter(s).items())
            if c not in cSet:
                cSet[c] = []
            cSet[c].append(s)
        
        return list(cSet.values())