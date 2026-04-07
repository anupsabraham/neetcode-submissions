class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_counter = defaultdict(int)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            char_counter[s[i]] += 1
            char_counter[t[i]] -= 1
        
        for char, count in char_counter.items():
            if count != 0:
                return False
        
        return True