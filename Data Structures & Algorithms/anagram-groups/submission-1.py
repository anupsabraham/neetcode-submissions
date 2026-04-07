class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashset = defaultdict(list)
        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c)-96] += 1
            
            hashset[str(count)].append(s)
        
        return [v for k, v in hashset.items()]
