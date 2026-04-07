class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashset = defaultdict(list)

        for s in strs:
            hashset[tuple(sorted(s))].append(s)
        
        return [v for x, v in hashset.items()]