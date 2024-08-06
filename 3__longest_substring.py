#1. Loop over string to check if next character in string was in the string
#2. 



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        lst = []
        big = 0
        slist = list(s)
        for i in range(len(slist)):
            if slist[i] in lst:
                lst = lst[lst.index(slist[i]) + 1:]  
                count = len(lst)
            lst.append(slist[i])
            count += 1
            if count > big:
                big = count
        return big
            
