class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        p = p.strip().split()
        s = s.strip().split()
        d = {}
        used = set()
        if len(p)!=len(s):
            return False
        else:
            for i in range(len(p)):
                if p[i] not in d:
                    if s[i] in used:
                        return False
                    d[p[i]] = s[i]
                    used.add(s[i])
                else:
                    if d[p[i]]!=s[i]:
                        return False
            else:
                return True