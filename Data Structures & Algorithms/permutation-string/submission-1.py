class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = 1
        while l < len(s2):
            s1_set = list(s1)
            r = l
            while r < len(s2):    
                if s2[r] in s1_set:
                    s1_set.remove(s2[r])
                else:
                    break
                if not s1_set:
                    return True
                r += 1
            else:
                if not s1_set:
                    return True
            l += 1
        return False
