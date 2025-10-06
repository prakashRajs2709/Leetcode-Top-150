class Solution:
    def singleNumber(self, n: List[int]) -> int:
        m=0
        for i in range(0,len(n)):
            m=n[i]^m
        return m
            
        