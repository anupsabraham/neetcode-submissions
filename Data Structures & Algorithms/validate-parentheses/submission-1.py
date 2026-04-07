class Solution:
    def isValid(self, s: str) -> bool:
        b = []

        mapping = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c not in mapping:
                b.append(c)
            else:
                if not b or b.pop() != mapping[c]:
                    return False

        return not b