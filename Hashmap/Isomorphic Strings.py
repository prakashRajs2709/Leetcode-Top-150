class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(t)!=len(s):
            return False
        s_to_t = {}
        t_to_s = {}
        for sc, tc in zip(s, t):
            if (sc in s_to_t and s_to_t[sc] != tc) or (tc in t_to_s and t_to_s[tc] != sc):
                return False
            s_to_t[sc] = tc
            t_to_s[tc] = sc

        return True