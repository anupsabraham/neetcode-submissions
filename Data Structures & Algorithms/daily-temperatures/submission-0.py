class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                stack_temp, stack_idx = stack.pop()
                out[stack_idx] = i - stack_idx
            stack.append((temperatures[i], i))
        return out