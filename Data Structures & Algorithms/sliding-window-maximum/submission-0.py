class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0

        q = deque()

        out = []

        while r < len(nums):
            # print(q)
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)
            
            if q[0] < l:
                q.popleft()

            if r+1 >= k:
                out.append(nums[q[0]])
                l += 1
            r += 1
            # print(q)
        
        return out
