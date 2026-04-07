class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        if len(s) <= 1:
            return len(s)
        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                if s[j] in s[i:j]:
                    max_len = max(max_len, j-i)
                    break
            else:
                max_len = max(max_len, j-i+1)

        return max_len