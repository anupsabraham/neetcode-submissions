class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = defaultdict(int)

        s_count = defaultdict(int)

        for c in t:
            t_count[c] += 1

        l = 0
        r = 0

        matches = 0

        ret_str = None

        shift_right = True 

        while r < len(s):
            if shift_right:
                c = s[r]
                if c in t_count:
                    s_count[c] += 1

                    if s_count[c] == t_count[c]:
                        matches += 1

            else:
                c = s[l-1]
                if c in t_count:
                    s_count[c] -= 1
                    if s_count[c] < t_count[c]:
                        matches -= 1

            if matches == len(t_count):
                new_str = s[l:r+1]
                if not ret_str:
                    ret_str = new_str
                elif len(ret_str) > len(new_str):
                    ret_str = new_str
                l += 1
                shift_right = False
            elif matches < len(t_count):
                r += 1
                shift_right = True

        return ret_str or ""
