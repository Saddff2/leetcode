#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
#An Anagram is a word or phrase formed by rearranging the letters
#of a different word or phrase, typically using all the original letters exactly once.


#1. list of all letters
#1.1 checksum of letters in the list
#2. check if all letters is in t
#3. check checksum

s="panama"
print(list(s))


class Solution:
    def isAnagram(self, s, t):
        s = sorted(s)
        t = sorted(t)
        return s == t
        