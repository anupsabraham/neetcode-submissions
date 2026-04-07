class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [1,2,4,6]

        [48,24,6,1]
        
        [1,1,2,8]

        [48, 24, 12, 8]
        """
        post_prod = [1]*len(nums)
        for i in range(len(nums)-2, -1, -1):
            post_prod[i] = post_prod[i+1] * nums[i+1]
        
        pre_prod = 1
        final_list = []
        for i in range(len(nums)):
            final_list.append(pre_prod*post_prod[i])
            pre_prod *= nums[i]
        
        return final_list