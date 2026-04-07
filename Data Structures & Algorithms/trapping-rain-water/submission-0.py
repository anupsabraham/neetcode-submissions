class Solution:
    def trap(self, height: List[int]) -> int:
        max_l = height[0]
        max_r = height[len(height)-1]
        l=0
        r=len(height)-1

        ret = 0
        while l<r:
            if max_l < max_r:
                l += 1
                max_l = max(max_l, height[l])
                ret += max_l - height[l]
            else:
                r -= 1
                max_r = max(max_r, height[r])
                ret += max_r - height[r]
        
        return ret
        