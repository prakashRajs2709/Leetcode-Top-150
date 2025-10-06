class Solution:
    def maxProfit(self, n: List[int]) -> int:
        lmin = float('inf')
        maxp = 0
        for i in n:
            lmin = min(lmin, i)
            maxp = max(maxp, i - lmin)
        return maxp