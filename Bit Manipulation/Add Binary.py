class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a,2)
        b = int(b,2)
        carry_n = a^b
        carry_y = (a&b)<<1
        a,b = carry_n,carry_y
        return bin(a+b)[2:]