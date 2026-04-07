class Solution:

    def encode(self, strs: List[str]) -> str:
        single_str = ""
        for s in strs:
            single_str += f"{len(s)}#{s}"
        return single_str

    def decode(self, s: str) -> List[str]:
        str_list = []

        i = 0
        while i < len(s):
            length = ""
            while s[i] != "#":
                length += s[i]
                i += 1
            length = int(length)
            i += 1
            str_list.append(s[i:i+length])
            i += length
        
        return str_list
