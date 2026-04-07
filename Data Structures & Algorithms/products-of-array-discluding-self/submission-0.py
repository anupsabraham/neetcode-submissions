class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_prod = [1] * len(nums)

        for i in range(1, len(nums)):
            pre_prod[i] = pre_prod[i-1] * nums[i-1]
        
        post_prod = 1
        ret = [1]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            ret[i] = pre_prod[i] * post_prod
            post_prod = post_prod * nums[i]
        
        return ret