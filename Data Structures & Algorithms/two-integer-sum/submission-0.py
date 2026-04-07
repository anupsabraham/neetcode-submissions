class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}

        for x in range(len(nums)):
            curr_val = nums[x]
            if curr_val in hashset:
                return [hashset[curr_val], x]
            hashset[target-curr_val] = x
        
        return []