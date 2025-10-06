class Solution:
    def climbStairs(self, n: int) -> int:
        def fu(n,memo):
            if n==0 or n==1:
                return 1
            if memo[n]!=-1:
                return memo[n]
            memo[n] =  fu(n-1,memo)+fu(n-2,memo)
            return memo[n]

        memo = [-1]*(n+1)
        return fu(n,memo)