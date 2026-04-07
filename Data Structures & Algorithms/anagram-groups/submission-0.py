class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashset = defaultdict(list)
        for s in strs:
            hashset["".join(sorted(s))].append(s)
        
        return [v for k, v in hashset.items()]
