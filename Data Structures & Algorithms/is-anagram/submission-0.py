class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for x in range(len(s)):
            s_dict[s[x]] += 1
            t_dict[t[x]] += 1
        
        for k, v in s_dict.items():
            if v != t_dict[k]:
                return False
        else:
            return True
