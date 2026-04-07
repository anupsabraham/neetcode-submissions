class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal_string = "".join([x.lower() for x in s if x.isalnum()])

        x = 0
        while x < len(pal_string)//2:
            if pal_string[x] != pal_string[len(pal_string)-1-x]:
                return False
            x += 1
        return True