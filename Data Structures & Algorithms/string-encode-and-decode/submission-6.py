class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for x in strs:
            out += str(len(x)) + "|" + x
        
        return out


    def decode(self, s: str) -> List[str]:
        out = []
        
        i = 0
        word_length = 0
        while i < len(s):
            if s[i] == "|":
                out.append(s[i+1:i+1+word_length])
                i = i + word_length + 1
                word_length = 0
            else:
                word_length = (word_length*10) + int(s[i])
                i += 1
        
        return out

