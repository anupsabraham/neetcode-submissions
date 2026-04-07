class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        n_set = set(nums)

        for x in n_set:
            if x-1 not in n_set:
                y = x
                length = 0
                while y in n_set:
                    y += 1
                    length += 1
                longest = max(longest, length)
        return longest
