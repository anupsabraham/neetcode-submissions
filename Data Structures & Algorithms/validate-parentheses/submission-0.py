class Solution:
    def isValid(self, s: str) -> bool:
        b = []

        for c in s:
            if c in "({[":
                b.append(c)
            else:
                if not b:
                    return False
                c_open = b.pop()
                
                if c == ")":
                    if c_open != "(":

                        return False
                elif c == "}":
                    if c_open != "{":
                        return False
                elif c == "]":
                    if c_open != "[":
                        return False
        
        return len(b) == 0