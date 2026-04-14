class Solution:
    def trap(self, height: List[int]) -> int:
        """
        0 2 0 3 1 0 1 3 2 1
        L                 R

        0 2 0 3 1 0 1 3 2 1
          L               R

        0 2 0 3 1 0 1 3 2 1
          L             R

            2
        0 2 0 3 1 0 1 3 2 1
            L           R

            2
        0 2 0 3 1 0 1 3 2 1
              L         R

            2
        0 2 0 3 1 0 1 3 2 1
              L       R

            2   2
        0 2 0 3 1 0 1 3 2 1
                L     R

            2   2 3
        0 2 0 3 1 0 1 3 2 1
                  L   R

        """
        max_left = 0
        max_right = 0

        left = 0
        right = len(height) - 1

        trapped_water = 0

        while left < right:
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])
            print(left, right, trapped_water, max_left, max_right)
            if height[left] <= height[right]:
                column_water = max(min(max_left, max_right) - height[left], 0)
                trapped_water += column_water
                
                left += 1
            else:
                column_water = max(min(max_left, max_right) - height[right], 0)
                trapped_water += column_water
                
                right -= 1

        return trapped_water