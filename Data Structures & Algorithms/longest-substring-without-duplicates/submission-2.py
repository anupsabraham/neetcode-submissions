class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        pwwkew
        
        l = p0
        r = p0

        sub_str = p
        r = w1
                = pw
        r = w2
                = pww
        max_len = 2

        """
        max_len = 0
        left = 0
        right = 0
        sub_str = ""
        while right < len(s):
            sub_str += s[right]
            max_len = max(max_len, len(set(sub_str)))
            if len(sub_str) != len(set(sub_str)):
                while left < right:
                    sub_str = s[left:right+1]
                    left += 1
                    if len(sub_str) == len(set(sub_str)):
                        break
            
            right += 1
        return max_len