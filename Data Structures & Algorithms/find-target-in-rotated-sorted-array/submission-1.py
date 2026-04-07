class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        [3, 5, 6, 0, 1, 2]
         0. 1. 2. 3. 4. 5
        target = 4

        l = 0
        r = 5
        m = 2

        target < n[m] and target < n[l]

        """
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r-l)//2
            # print(l, m, r)

            if target == nums[m]:
                return m
            
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
            # print(l, m, r, "modified")
        
        return -1