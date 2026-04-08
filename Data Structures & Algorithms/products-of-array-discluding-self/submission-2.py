class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1]*len(nums)

        pre = 1
        for i in range(0, len(out)-1):
            pre *= nums[i]
            out[i+1] = pre

        post = 1
        for i in range(len(out)-1, 0, -1):
            post *= nums[i]
            out[i-1] *= post
        
        return out