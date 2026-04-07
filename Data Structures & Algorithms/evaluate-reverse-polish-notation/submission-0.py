class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []

        for t in tokens:
            try: 
                t = int(t)
                nums.append(t)
            except ValueError:
                n2 = nums.pop()
                n1 = nums.pop()
                if t == "+":
                    nums.append(n1+n2)
                elif t == "-":
                    nums.append(n1-n2)
                elif t == "*":
                    nums.append(n1*n2)
                elif t == "/":
                    nums.append(int(n1/n2))
        
        return nums[0]