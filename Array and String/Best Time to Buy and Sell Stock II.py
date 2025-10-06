class Solution:
    def maxProfit(self, n: List[int]) -> int:
        r = 0
        for i in range(1,len(n)):
            if n[i]>n[i-1]:
                r = r + (n[i] - n[i-1])
        return r
