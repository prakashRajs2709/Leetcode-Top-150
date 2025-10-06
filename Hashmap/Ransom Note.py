class Solution:
    def canConstruct(self, ransom: str, magazine: str) -> bool:
        r = Counter(ransom)
        m = Counter(magazine)
        for char,count in r.items():
            if m[char]<count:
                return False
        return True