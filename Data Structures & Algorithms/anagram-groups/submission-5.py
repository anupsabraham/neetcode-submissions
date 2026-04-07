class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        counter = [1,0,1,0,0,0,0,0,0,0,.... 1[t],0,0...] act
        """
        groups = defaultdict(list)
        for s in strs:
            counter = [0]*26
            for c in s:
                counter[ord(c)-ord('a')] += 1
            
            groups["|".join([str(x) for x in counter])].append(s)
        
        return [x for x in groups.values()]
