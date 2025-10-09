def roman_to_integer(num)-> int:
    result = 0
    intmap = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    for i in range(len(num)):
        if i>0 and intmap[num[i]]>intmap[num[i-1]]:
            result = result + intmap[num[i]] - 2 * intmap[num[i-1]]
        else:
            result = result + intmap[num[i]]
    return result





num = 'XIV'
print(roman_to_integer(num))