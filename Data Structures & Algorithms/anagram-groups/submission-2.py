class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #This is grouping problem where we benefit from finding one identifier and appending values to it.
        d = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            d[sortedS].append(s)
        return list(d.values())