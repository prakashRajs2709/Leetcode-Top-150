class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=''
        for i in digits:
            num = num+str(i)
        num = int(num)
        num+=1
        num = list(str(num))
        dig = []
        for i in num:
            dig.append(int(i))
        return(dig)