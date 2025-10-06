class Solution:
    def singleNumber(self, n: List[int]) -> int:
        ones = 0
        twos = 0
        for num in n:
            ones = ones ^ (num & ~twos)
            twos = twos ^ (num & ~ones)
        return ones

        

        